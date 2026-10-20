#!/usr/bin/env python3
"""Check the finished PDF for margin-note layout faults.

usage: scripts/check_margins.py [PDF] [--preamble preamble.tex]

Margin notes are LaTeX \\marginpar floats. Two things can go wrong with them:

* A note that does not fit at the bottom of a page is deferred to the next page but keeps the side
  of the old page, so on the next page it lands in the inner (gutter) margin, squeezed and clipped
  by the page edge.
* Notes can hang far below the text block, overlap each other, or collide with body text.

A note deferred to the wrong side is partly clipped off the page, and PDF text extraction cannot even
see clipped text, so that case is detected from the rendered pixels (ink in the inner margin).

This script reports every such page. It needs only Python 3 and poppler (``pdftotext``, ``pdftoppm``). The page
geometry is read from the ``geometry`` options in preamble.tex, so it follows any layout change.

Fix a problem by lifting the note with \\mshift{<length>} immediately before it, or by moving the
note to a later paragraph. Exit status is 1 if any fault is found.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
from html import unescape
from pathlib import Path

MM = 72 / 25.4
DEFAULT_PDF = "operator-algebra-modular-theory-and-quantum-gravity.pdf"
HANG_LIMIT_MM = 262.0      # lowest allowed bottom edge of a margin note (page height is 285 mm)
HEADER_MM = 25.0           # anything above this is the running header


def read_geometry(preamble):
    text = Path(preamble).read_text()
    m = re.search(r"\\usepackage\[([^\]]*)\]\{geometry\}", text)
    if not m:
        sys.exit("check_margins: no geometry options found in %s" % preamble)
    opts = dict(
        (k.strip(), v.strip())
        for k, v in (o.split("=", 1) for o in m.group(1).split(",") if "=" in o)
    )

    def mm(key):
        return float(opts[key].replace("mm", ""))

    return dict(
        W=mm("paperwidth"), H=mm("paperheight"), inner=mm("inner"),
        text=mm("textwidth"), sep=mm("marginparsep"), mp=mm("marginparwidth"),
    )


def read_pages(pdf):
    out = subprocess.run(["pdftotext", "-bbox-layout", str(pdf), "-"],
                         capture_output=True, text=True, check=True).stdout
    pages = []
    for pg in re.split(r"<page ", out)[1:]:
        blocks = []
        for b in re.finditer(r'<block xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</block>', pg, re.S):
            x0, y0, x1, y1 = (float(v) / MM for v in b.groups()[:4])
            words = [unescape(w) for w in re.findall(r"<word[^>]*>(.*?)</word>", b.group(5))]
            blocks.append((x0, y0, x1, y1, " ".join(words)))
        pages.append(blocks)
    return pages


def printed_label(blocks):
    for x0, y0, x1, y1, txt in blocks:
        if y0 < HEADER_MM and re.fullmatch(r"\d+", txt.strip()):
            return txt.strip()
    return None


def gutter_ink_pages(pdf, g, dpi=30, threshold=3):
    """Pages with dark pixels in the inner (gutter) margin, where nothing should ever be printed."""
    tmp = tempfile.mkdtemp()
    try:
        subprocess.run(["pdftoppm", "-gray", "-r", str(dpi), str(pdf), os.path.join(tmp, "p")], check=True)
        bad = []
        for f in sorted(os.listdir(tmp)):
            m = re.search(r"-(\d+)\.pgm$", f)
            if not m:
                continue
            n = int(m.group(1))
            data = open(os.path.join(tmp, f), "rb").read()
            hdr = re.match(rb"P5\s+(\d+)\s+(\d+)\s+(\d+)\s", data)
            w, h = int(hdr.group(1)), int(hdr.group(2))
            px = data[hdr.end():]
            y0, y1 = int(HEADER_MM / g["H"] * h), int(HANG_LIMIT_MM / g["H"] * h)
            x_in = int((g["inner"] - 2) / g["W"] * w)
            cols = range(0, x_in) if n % 2 == 1 else range(w - x_in, w)
            dark = sum(1 for y in range(y0, y1) for x in cols if px[y * w + x] < 160)
            if dark > threshold:
                bad.append(n)
        return bad
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def check(pdf, preamble):
    g = read_geometry(preamble)
    pages = read_pages(pdf)
    problems = []
    for i, blocks in enumerate(pages):
        n = i + 1
        odd = n % 2 == 1
        if odd:   # recto: inner margin on the left, notes on the right
            text_a, text_b = g["inner"], g["inner"] + g["text"]
            marg_a, marg_b = text_b + g["sep"], text_b + g["sep"] + g["mp"]
            gutter = lambda cx: cx < g["inner"]
        else:     # verso: notes on the left
            text_b = g["W"] - g["inner"]; text_a = text_b - g["text"]
            marg_b = text_a - g["sep"]; marg_a = marg_b - g["mp"]
            gutter = lambda cx: cx > g["W"] - g["inner"]
        lab = printed_label(blocks)
        tag = "PDF page %d%s" % (n, " (printed %s)" % lab if lab else "")
        body = [b for b in blocks if b[1] >= HEADER_MM]
        margin = []
        for x0, y0, x1, y1, txt in body:
            cx = (x0 + x1) / 2
            if x1 > g["W"] + 0.5 or x0 < -0.5:
                problems.append((n, tag, "note clipped by the page edge: '%s...'" % txt[:40]))
            if gutter(cx):
                problems.append((n, tag, "note on the wrong (inner) side, probably deferred from the previous page: '%s...'" % txt[:40]))
            elif marg_a - 1 <= cx <= marg_b + 1 and ((x0 > text_b - 5) if odd else (x1 < text_a + 5)):
                margin.append((x0, y0, x1, y1, txt))
        margin.sort(key=lambda b: b[1])
        for b in margin:
            if b[3] > HANG_LIMIT_MM:
                problems.append((n, tag, "note hangs to %.0f mm (limit %.0f): '%s...'" % (b[3], HANG_LIMIT_MM, b[4][:40])))
        for a, b in zip(margin, margin[1:]):
            if b[1] < a[3] - 1.0 and min(a[2], b[2]) - max(a[0], b[0]) > 5:
                problems.append((n, tag, "two notes overlap: '%s...' and '%s...'" % (a[4][:25], b[4][:25])))
        for x0, y0, x1, y1, txt in body:
            if (x0, y0, x1, y1, txt) in margin:
                continue
            reach = x1 if odd else x0
            into = reach > marg_a + 1 if odd else reach < marg_b - 1
            if into and not gutter((x0 + x1) / 2):
                for m in margin:
                    if y0 < m[3] and y1 > m[1]:
                        problems.append((n, tag, "body text runs into a margin note: '%s...'" % txt[:40]))
                        break
    labels = {i + 1: printed_label(b) for i, b in enumerate(pages)}
    for n in gutter_ink_pages(pdf, g):
        lab = labels.get(n)
        tag = "PDF page %d%s" % (n, " (printed %s)" % lab if lab else "")
        problems.append((n, tag, "ink in the inner margin: a margin note was deferred to the wrong side and is clipped by the page edge"))
    return problems, len(pages)


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    pdf = args[0] if args else DEFAULT_PDF
    pre = "preamble.tex"
    if "--preamble" in argv:
        pre = argv[argv.index("--preamble") + 1]
        args = [a for a in args if a != pre]
        pdf = args[0] if args else DEFAULT_PDF
    problems, npages = check(pdf, pre)
    print("margins: %d pages checked, %d problem(s)" % (npages, len(problems)))
    seen = set()
    for n, tag, msg in problems:
        if (n, msg) in seen:
            continue
        seen.add((n, msg))
        print("  %s: %s" % (tag, msg))
        if "GITHUB_ACTIONS" in os.environ:
            print("::error::%s: %s" % (tag, msg))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

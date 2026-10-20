# Operator Algebras, Modular Theory, and Quantum Gravity: A Physicist's Guide

A free-standing textbook, written in LaTeX, that teaches the mathematics of *operator algebras* to physicists and uses it to explain a recent idea in quantum gravity: that, once gravity and an observer are taken into account, the quantum description of a region of space-time changes character in a precise and computable way.

This repository contains the full source of the book, the scripts that assemble it, and an automated pipeline that compiles it into a PDF and publishes that PDF on GitHub.

## At a glance

| | |
|---|---|
| **What it is** | A textbook of about 190 pages with exercises and worked solutions |
| **Who it is for** | Physicists with a graduate-level background in quantum mechanics and quantum field theory (some statistical mechanics and general relativity helps). No prior training in functional analysis or topology is assumed. |
| **Where to read it** | The compiled PDF on the [Releases page](https://github.com/saeidaliei/opalgebra-book/releases) (see [Get the book](#get-the-book)) |
| **Format** | LaTeX source, built with `make` or by GitHub Actions |
| **Authors** | Claude Sonnet (an AI language model made by Anthropic), with supervision of Saeid Aliei |
| **Status** | Complete draft; not independently peer reviewed (see [Status and scope](#status-and-scope)) |
| **License** | None chosen yet (see [Citation and license](#citation-and-license)) |

## What the book is about

In quantum field theory, the observables localized in a region of space form a mathematical structure called an *operator algebra*. For regions with a boundary, this algebra is of a type (called type III) in which the usual notions of density matrix and entanglement entropy are not defined. Recent work, building on Witten's *crossed product* construction, shows that when gravity is included, and an observer is added to the description, the algebra changes to a type (type II) in which entropy is well defined. In de Sitter space (a model of an expanding universe with a cosmological horizon), the construction of Chandrasekaran, Longo, Penington and Witten (called **CLPW** below) gives an algebra of type II$_1$ with a state of maximal entropy, which is the empty de Sitter space itself.

The book builds up everything needed to understand this statement, with the physical motivation first and the mathematics second:

1. the functional analysis that quantum mechanics quietly relies on;
2. C$^*$-algebras and von Neumann algebras, and their classification into types I, II and III;
3. modular (Tomita–Takesaki) theory, which attaches a canonical "time evolution" to any state and explains thermal equilibrium without a Hamiltonian;
4. crossed products, algebraic quantum field theory, and the CLPW algebra;
5. black holes, holography, and Connes' noncommutative geometry, treated more briefly.

## Get the book

You do not need to compile anything to read it.

* **Latest build:** open the [Releases page](https://github.com/saeidaliei/opalgebra-book/releases) and download the PDF attached to the release called **latest**. It is rebuilt automatically from the `main` branch every time the source changes.
* **Numbered versions:** releases named `v1.0.0`, `v1.1.0`, and so on are permanent snapshots. Use these when you need something stable to cite.

## Contents

The book has 13 chapters, arranged in parts, plus appendices.

| Part | Chapters | Main topics |
|---|---:|---|
| Prelude | 1 | Motivation and how to use the book |
| Mathematical toolkit | 2 | Hilbert spaces, operator topologies, the spectral theorem, Weyl relations, groups, positive energy |
| C$^*$-algebras | 3 | States, the GNS construction, inequivalent representations, thermodynamic limits |
| von Neumann algebras | 4 | Double commutant theorem, factors, traces, types I/II/III, entanglement |
| Modular theory | 5 | KMS states, Tomita–Takesaki theory, modular Hamiltonians, relative entropy, Connes' classification |
| Crossed products | 6 | Crossed products, Takesaki duality, entropy in type II, clock models |
| Algebraic quantum field theory | 7 | Haag–Kastler axioms, Reeh–Schlieder and Bisognano–Wichmann theorems, type III$_1$, superselection sectors |
| Gravity and de Sitter space | 8–10 | Constraints, edge modes, the CLPW algebra, observers, generalized entropy, open questions |
| Black holes and holography | 11 | Large-$N$ methods, black-hole crossed products, entanglement wedges, Hawking radiation |
| Noncommutative geometry | 12 | Spectral triples, Dixmier trace, spectral action, the Standard Model, thermal time |
| Frontiers | 13 | Open problems and a guide to the recent literature |

The appendices (A–I) cover topology, measure theory and distributions, groups and Haar measure, heat kernels, Clifford algebras, solutions to all exercises, notation, a glossary relating mathematical and physical terms, and an annotated bibliography.

Section 1.2 of the book proposes several reading paths. Readers interested mainly in the CLPW construction can follow the material marked `core`; some sections are marked as skippable on a first reading.

## Build the book from source

### Requirements

* `make` and Python 3
* A TeX Live installation that provides `pdflatex`, `latexmk`, `bibtex` and `makeindex`, with the usual packages and fonts

A full TeX Live installation (or MacTeX on macOS, or TeX Live inside WSL on Windows) is the simplest option. On Ubuntu or Debian the following is sufficient, and it is what the automated build installs:

```sh
sudo apt-get install latexmk make python3 poppler-utils \
  texlive-base texlive-latex-base texlive-latex-recommended \
  texlive-latex-extra texlive-fonts-recommended texlive-pictures
```

### Commands

Run these from the repository root.

```sh
make          # build the whole book
make check    # build, then fail on unresolved references/citations or margin-note faults
make ch N=9   # build only chapter 9 (fast; cross-references to other chapters stay unresolved)
make clean    # remove the PDF, LaTeX auxiliary files, and scratch files
```

The result is `operator-algebra-modular-theory-and-quantum-gravity.pdf` in the repository root. There is no separate preparation step: `make` regenerates the top-level `main.tex` from the sources whenever they change.

## Automated builds and releases

The workflow in `.github/workflows/build-book.yml` runs on GitHub Actions. It compiles the book on Ubuntu 24.04 (TeX Live 2023) and publishes the result:

| Event | What happens |
|---|---|
| Push to the `main` branch | The PDF is rebuilt and attached to the release named **latest**, which is replaced each time. |
| Push of a tag starting with `v` | The PDF is attached to a permanent release named after the tag, with automatically generated notes. |
| Pull request | The book is compiled and checked; the PDF is kept as a downloadable workflow artifact but no release is created. |

To publish a numbered version:

```sh
git tag v1.0.0
git push origin v1.0.0
```

Every build fails if the LaTeX log reports an unresolved reference or citation, or if a margin note is misplaced (see [Editing the book](#editing-the-book)). Each run also reports the page count and the number of overfull boxes (lines that stick out into the margin) in the job summary. Creating releases needs write access for the workflow: if it fails with a permissions error, enable read and write permissions under *Settings → Actions → General → Workflow permissions*.

## Repository layout

```text
.
├── .github/workflows/
│   └── build-book.yml     Compile, check, and publish the PDF
├── chapters/              The 13 chapters (one LaTeX file each)
├── appendices/            Appendices A–I
├── parts/                 Part introductions and "dictionary" boxes
├── frontmatter/           Title page and preface
├── scripts/
│   ├── gen.py             Generates main.tex from the files below
│   ├── chapters.tsv       Chapter list, titles, and reading-path labels
│   ├── parts.tsv          Part list and titles
│   ├── chapter_only.py    Builds a single chapter (used by `make ch`)
│   ├── check_log.sh       Quality gate on the LaTeX log (used by CI and `make check`)
│   ├── check_margins.py   Finds misplaced margin notes in the finished PDF (used by CI and `make check`)
│   ├── check_toy.py       Numerical check of the crossed-product toy model
│   └── check_clpw_general.py   Numerical check of the CLPW entropy formula
├── preamble.tex           Packages, page layout, boxes and environments
├── macros.tex             Mathematical notation macros
├── refs.bib               Bibliography database
├── main.tex               Generated top-level file (do not edit by hand)
├── Makefile               Build, check, and cleanup targets
└── .gitignore             Excludes LaTeX build products and the PDF
```

## Editing the book

* **Adding or reordering chapters.** Edit `scripts/chapters.tsv` (and `scripts/parts.tsv` for parts); `main.tex` is regenerated automatically. Each chapter file is plain LaTeX in `chapters/`.
* **Notation.** Shared notation macros (number sets, Hilbert-space operators, algebras, states and so on) live in `macros.tex`, and Appendix G lists them; use them rather than writing notation inline.
* **Boxes.** `preamble.tex` defines the recurring environments: `physmotiv` (the "Physics motivation" note that opens most sections), `keyidea` (a highlighted key point), `whatwrong` ("What could go wrong": common misconceptions), `unsettled` ("Status of the literature": marks results that are still debated), and `dictbox` (a physics–mathematics dictionary).
* **Margin material.** The pages have a wide outer margin in the style of Edward Tufte's books. Besides `\sidenote`, three macros in `preamble.tex` place material there:

  ```latex
  \mnote[Who]{A short history note, a recalled definition, or an at-a-glance result.}
  \mfig{\begin{tikzpicture} ... \end{tikzpicture}}{Caption.}   % optional first argument: width
  \mshift{20mm}   % goes immediately before a note and lifts it by 20 mm
  ```

  Margin notes are `\marginpar`s, so they stack and never overlap. If a note sits so close to the bottom of a page that it hangs below the text, `\mshift` lifts it. The proportions of text and margin are set in one line, the `geometry` options in `preamble.tex` (`textwidth`, `marginparwidth`).
* **Margin-note faults.** A margin note that does not fit at the bottom of a page is moved by LaTeX to the next page but keeps the old page's side, so it ends up squeezed into the inner margin and cut off by the page edge. This can reappear whenever text is added or removed. `scripts/check_margins.py` finds it (and notes that hang too low, overlap each other, or collide with body text) and prints the PDF page and the printed page number. To fix a reported note, put `\mshift{<length>}` immediately before it, or move it to a later paragraph.
* **Checking your changes.** Run `make check` before pushing; it is the same set of tests that the automated build applies.

## Numerical checks

Two scripts (they need Python 3 and NumPy) test calculations from the text against direct numerical computation:

```sh
python3 scripts/check_toy.py
python3 scripts/check_clpw_general.py
```

The first verifies the finite-dimensional crossed-product example of Chapter 6: its entropy formula, trace weight and flow conventions. The second tests the CLPW entropy formula of Chapter 9 in a type I model for selected states.

## Status and scope

* The book is a complete draft that has not undergone independent peer review. Errors may remain, and corrections are welcome (see below).
* Chapter 9, including the worked example in Section 9.3, follows the CLPW paper ([arXiv:2206.10780](https://arxiv.org/abs/2206.10780)); the notation guide and the entropy formula were checked against it, and the formula also has a numerical test. The discussion of later sections of that paper is limited to the material in its published text, and conjectural claims are presented as conjectures.
* Chapters 8–11 and the Lorentzian-signature section of Chapter 12 cover research from 2021 onward. Where results or interpretations are still debated, the text says so in a marked box.
* Appendix F gives a solution to every exercise. The solutions concentrate on the main argument and may omit routine intermediate steps.

## Feedback and contributions

Please open an issue on GitHub for errors, unclear explanations, or missing references, and include the chapter or section number. Pull requests are welcome; run `make check` first.

## Citation and license

When citing the book, give the release tag or commit used and this repository's URL. A suggested form:

```bibtex
@misc{opalgebra-book,
  title        = {Operator Algebras, Modular Theory, and Quantum Gravity: A Physicist's Guide},
  author       = {{Claude Sonnet} and Aliei, Saeid},
  howpublished = {\url{https://github.com/saeidaliei/opalgebra-book}},
  note         = {Release v1.0.0}
}
```

No license has been chosen yet. Until one is added to the repository, the default copyright rules apply: you may read the book and build it for personal use, but redistribution or reuse of the text requires permission from the repository owner.

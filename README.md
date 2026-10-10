# Operator Algebras, Modular Theory, and Quantum Gravity: A Physicist's Guide

A graduate-level LaTeX book (about 200 pages, 13 chapters, 205 exercises with complete solutions) that teaches the operator-algebraic
tools behind recent work on quantum gravity: von Neumann algebras, Tomita-Takesaki
modular theory, crossed products, and their use in the de Sitter "algebra of observables"
of Chandrasekaran, Longo, Penington and Witten (CLPW). It is written for physicists.

## Who it is for
Readers with graduate quantum mechanics, quantum field theory, and some statistical
mechanics and general relativity, but **no** formal training in functional analysis or
topology. The goal is that such a reader can follow Witten's crossed-product paper
("Gravity and the crossed product") and the CLPW paper on de Sitter space.

## What it covers
Thirteen chapters, grouped into eleven Parts (numbered 0 to X). Each chapter is made of
short sections (the units of the original outline), each opening with a margin note
"Physics motivation", containing a "What could go wrong" box where useful, and ending
with exercises.

| Part | Chapter | Content |
|---|---|---|
| 0 Prelude | 1 Why algebras, and how to read this book | motivation, the story in one page, reading paths, conventions |
| I Toolkit | 2 The mathematical toolkit | Hilbert space, operator topologies, spectral theorem, Weyl relations, groups and positive energy |
| II C*-algebras | 3 C*-algebras, states, and representations | states, GNS, inequivalent representations, thermodynamic limit |
| III von Neumann | 4 von Neumann algebras | double commutant, factors, traces, types I/II/III, entanglement |
| IV Modular theory | 5 Equilibrium and modular theory | KMS, Tomita-Takesaki, modular Hamiltonian, relative entropy, Connes classification |
| V Crossed products | 6 Crossed products | crossed product, Takesaki duality, entropy in type II, clock toy models |
| VI AQFT | 7 Algebraic quantum field theory | Haag-Kastler, Reeh-Schlieder, Bisognano-Wichmann, type III_1, DHR |
| VII Gravity | 8 Gravity, constraints, and de Sitter space | constraints, edge modes, static patch, the observer |
| | 9 The CLPW algebra | the type II_1 algebra, maximum-entropy state, entropy formula |
| | 10 Observers, entropy, and open questions | clocks, what is an observer, generalized entropy, open problems |
| VIII Black holes | 11 Black holes and holography | large N, black-hole crossed product, entanglement wedges, Hawking radiation |
| IX NCG | 12 Intermezzo: noncommutative geometry | spectral triples, Dixmier trace, spectral action, Standard Model, thermal time |
| X Frontiers | 13 Frontiers | open problems; guide to the recent literature |

Appendices: topology and measure-theory crash courses, groups, heat kernels, Clifford
algebras, solutions to every exercise, a notation table, a math-physics glossary, and an annotated
bibliography. There is an index and a bibliography (`refs.bib`).

**Reading paths.** Section 1.2 gives four reading paths. Material tagged `core` in
`scripts/chapters.tsv` is the fast track to CLPW; sections marked "can be skipped on a
first reading" (Weyl relations, superselection, black holes, noncommutative geometry)
can be left out. Each Part ends with a physics-math dictionary.

Sections added beyond the original outline: self-adjoint extensions and the half-line
clock (2.6), dimension and the hyperfinite II_1 factor (4.6), monotonicity of relative
entropy (5.5), a worked qubit-plus-clock example (9.3), black-hole versus de Sitter
thermodynamics (11.5), and two spectral-action computations (12.9).

## Typography and layout
The page design follows J. Schwichtenberg, *Physics from Symmetry*: Palatino text with
Pazo math, a text block pushed toward the inner edge, a wide outer margin holding
sidenotes, "Physics motivation" notes and figure captions, small-caps running heads,
and bold old-style chapter and section numerals (see `preamble.tex`). The page is
215 x 285 mm.

## Conventions
Locked in `macros.tex` and summarized in Appendix "Notation". The key ones for the
gravity chapters: modular Hamiltonian `K = -log Delta` (`K = beta_dS H` in de Sitter);
crossed-product variables `x = -beta_dS q`, `X = K + x`, `p = -i d/dx`; trace weight
`tau(a) = int dx e^x <a(x)>`; the maximal-entropy state has density matrix equal to the
identity of the type II_1 algebra. Section 9.1 contains a dictionary to the CLPW paper's
own notation.

## How to compile
Requirements: a TeX Live installation with `pdflatex`, `latexmk` and `bibtex`
(plus `makeindex`, which latexmk calls), and Python 3.

```
make            # builds main.pdf (runs scripts/gen.py, then latexmk)
make ch N=9     # build a single chapter quickly (scripts/chapter_only.py)
make clean      # remove build products
```

`main.tex` is **generated** by `scripts/gen.py` from `scripts/chapters.tsv` and
`scripts/parts.tsv`; edit those (or the files under `chapters/`, `parts/`,
`appendices/`, `frontmatter/`), not `main.tex`. A full build takes a minute or two and
needs several LaTeX passes, which latexmk handles.

## Repository layout
```
main.tex            generated top-level file
preamble.tex        packages and boxes (physmotiv, whatwrong, keyidea, exercise, ...)
macros.tex          notation macros (do not redefine ad hoc)
refs.bib            bibliography (see "Verification" below)
chapters/           ch01_intro .. ch13_frontiers, one file per chapter
parts/              part dictionaries
appendices/         appendices A-I
frontmatter/        title, preface
figures/            (figures are drawn inline with TikZ)
scripts/            gen.py, chapter_only.py, chapters.tsv (13 chapters and the old
                    topics merged into each), parts.tsv,
                    check_toy.py, check_clpw_general.py
```

## Numerical checks
Two scripts (NumPy only) test claims of the text:
* `python3 scripts/check_toy.py` -- the finite-dimensional crossed product of Sec. 6.3-6.4:
  entropy formula, trace weight, and flow conventions.
* `python3 scripts/check_clpw_general.py` -- the CLPW entropy formula
  `S = h(g) + <X> - S_rel(Phi||Psi)` (Sec. 9.2) for a *general* state in a type I model:
  exact for `Phi = u Omega`, with error shrinking like 1/width^2 otherwise.

## Verification and scope notes
* Chapter 9 (including the worked qubit example in Sec. 9.3) was checked against the CLPW paper (arXiv:2206.10780); the
  conventions dictionary in Sec. 9.1 was verified, and the entropy formula in Sec. 9.2 was tested
  numerically. For the paper's Sec. 4.3-4.4 and 5 only the content reported in the
  paper's text and excerpts was available, so those parts (the no-observer conjecture,
  the Euclidean argument, the black-hole comparison) are summarized at that level of
  detail and attributed as conjectures where the paper does so.
* `refs.bib`: entries whose `note` field says "verified" were checked against journal
  records (Springer/INSPIRE reference lists). The remaining entries are standard
  citations (Bisognano-Wichmann, DHR, Haagerup, Pusz-Woronowicz, Kay-Wald, JLMS,
  Engelhardt-Wall, Connes, ...) whose details were not re-checked; confirm them before
  citing in a publication.
* Sections on very recent research (Chapters 8-11 and Sec. 12.8) are flagged with
  "unsettled" boxes where the literature is still moving.
* Every exercise has a written solution (Appendix F); solutions are condensed (the key
  computation or argument) and were re-derived, several numerically. While writing them
  two exercise statements were found wrong and corrected (a sign convention in the
  clock section 8.3 and an energy-spectrum condition in Sec. 4.3). The index is
  generated semi-automatically and is not exhaustive.
* The text has not been through independent peer review; errors are possible.
  Corrections are welcome.

## License / citation
No license has been specified. If you cite the book, cite the version of `main.pdf` you
used together with the commit or archive you obtained it from.

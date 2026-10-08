# STATUS (update after EVERY chapter written; this file is how the next session resumes)

## How to resume
1. Read STYLE.md and this file.
2. `python3 scripts/gen.py` regenerates main.tex and creates stubs for any missing chapters (never overwrites).
3. Pick the first chapter below with status != DONE (go in order; later chapters rely on earlier notation).
4. Write it following the template; compile with `python3 scripts/chapter_only.py N`; fix errors.
5. Flip its status here; add new bib entries to refs.bib (VERIFY flag if from memory).
6. After finishing a Part, write parts/partX_dictionary.tex (dictbox) and re-run gen.py.

Status values: STUB -> DRAFT (written, not reviewed) -> DONE (reviewed, compiles).
Each chapter file's first line is `% STATUS: ...` (keep in sync).

## Progress (end of session 1)
ALL 54 chapters, 8 appendices, preface and Part I-VII dictionaries are written (DRAFT). Book builds to ~225 pages with no undefined refs/cites.
- Ch 01 why_algebras: DRAFT (core)
- Ch 02 punchline: DRAFT (core)
- Ch 03 hilbert: DRAFT (core)
- Ch 04 topologies: DRAFT (core)
- Ch 05 spectral: DRAFT (core)
- Ch 06 weyl: DRAFT (skip)
- Ch 07 groups: DRAFT (core)
- Ch 08 cstar: DRAFT (core)
- Ch 09 states: DRAFT (core)
- Ch 10 gns: DRAFT (core)
- Ch 11 inequiv: DRAFT (core)
- Ch 12 quasilocal: DRAFT (core)
- Ch 13 doublecomm: DRAFT (core)
- Ch 14 factors: DRAFT (core)
- Ch 15 traces: DRAFT (core)
- Ch 16 classification: DRAFT (core)
- Ch 17 subsystems: DRAFT (core)
- Ch 18 kms: DRAFT (core)
- Ch 19 tomita: DRAFT (core)
- Ch 20 modham: DRAFT (core)
- Ch 21 connes_class: DRAFT (core)
- Ch 22 crossed: DRAFT (core)
- Ch 23 takesaki: DRAFT (core)
- Ch 24 entropy_II: DRAFT (core)
- Ch 25 toy_clock: DRAFT (core)
- Ch 26 haagkastler: DRAFT (core)
- Ch 27 rs_bw: DRAFT (core)
- Ch 28 typeIII_local: DRAFT (core)
- Ch 29 dhr: DRAFT (skip)
- Ch 30 gravity_constraints: DRAFT (core)
- Ch 31 gauge_warmup: DRAFT (core)
- Ch 32 ds_special: DRAFT (core)
- Ch 33 static_patch: DRAFT (core)
- Ch 34 add_observer: DRAFT (core)
- Ch 35 clpw: DRAFT (core)
- Ch 36 anatomy: DRAFT (core)
- Ch 37 clocks_qrf: DRAFT (core)
- Ch 38 what_observer: DRAFT (core)
- Ch 39 gen_entropy: DRAFT (core)
- Ch 40 open_ds: DRAFT (core)
- Ch 41 large_N: DRAFT (skip)
- Ch 42 bh_crossed: DRAFT (skip)
- Ch 43 ew_qec: DRAFT (skip)
- Ch 44 curved_hawking: DRAFT (skip)
- Ch 45 gelfand: DRAFT (skip)
- Ch 46 spectral_triples: DRAFT (skip)
- Ch 47 dixmier: DRAFT (skip)
- Ch 48 spectral_action: DRAFT (skip)
- Ch 49 almost_comm: DRAFT (skip)
- Ch 50 lorentzian_nc: DRAFT (skip)
- Ch 51 thermal_time: DRAFT (skip)
- Ch 52 bridge: DRAFT (skip)
- Ch 53 open_all: DRAFT (core)
- Ch 54 literature: DRAFT (core)

## What 'DRAFT' means here (be honest about confidence)
- HIGH confidence (derived/cross-checked, numerics in scripts/check_toy.py): Ch 1-25 mathematics, esp. Ch 19-25 conventions.
- MEDIUM: Ch 26-29 (AQFT; standard theorems stated from memory, hedged where hypotheses vary: Summers-Werner, III_1 for double cones, BW).
- MEDIUM-LOW (follow abstracts/structure of papers; only partly verified): Ch 30-40. Verified by web search: CLPW (JHEP 02(2023)082, II_1, max-entropy state), JSS (2306.01837), Faulkner-Speranza (2405.00847), De Vuyst et al (2405.00114, 2412.15502), Chen-Penington (2406.02116). Kirklin 2412.01903 title only. Witten background-independent algebra: NOT verified.
- LOW (condensed surveys from memory, need verification pass): Ch 41-44 (holography), Ch 45-52 (NCG; esp. Ch 49 Standard Model/Higgs-mass claims), Ch 44 ANEC/QNEC attributions, Ch 52 MIP*=RE statement.
- Ch 36 'anatomy' derivation of S_gen from the crossed-product entropy is a heuristic sketch; the careful derivation is in CLPW. REWRITE after reading CLPW Sec. 3-4 carefully (check signs: our x = -beta q, tau weight e^{x}, max-entropy density matrix P).
- Ch 38/40 are deliberately question-style (open problems).

## TODO for next session (priority order)
1. Verification pass on refs.bib: every entry with VERIFY (Bisognano-Wichmann, DHR, Haagerup, CCM, Leutheusser-Liu, Witten 2018/2021, etc.). Add Kay-Wald, Borchers-Buchholz, Buchholz-D'Antoni-Longo, Pusz-Woronowicz, Summers-Werner, Ceyhan-Faulkner, JLMS, Engelhardt-Wall, Penington, AEMM, Ji et al MIP*=RE, Connes reconstruction, CCvS 'Beyond the spectral SM' with real entries and add \cite calls in the text where names are mentioned.
2. Read CLPW fully and rewrite Ch 35-36 against it (notation, trace formula, regime of validity, role of mass of observer, SO(d-1) rotations).
3. Hostile exercise audit: solve each exercise at least sketchily; several (e.g. Ch 19 ex 4, Ch 27 ex 1, Ch 32 ex 2, Ch 45-48) are unchecked.
4. Add TikZ/figures: Penrose diagram of dS (exists, crude), modular flow picture, crossed-product schematic.
5. Overfull hbox cleanup (about 50 warnings), index, and a proper notation table.
6. Light spots: Ch 11 Goldstone sentence; Ch 17 Summers-Werner hypotheses; Ch 12 KMS simplex; Ch 21 T-invariant III_0; Ch 22 Powers factor centre remark; Ch 28 'hyperfinite III_1' attributions.
7. Consider moving Part IX before/after per user preference (currently after gravity).

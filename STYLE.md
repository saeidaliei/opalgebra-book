# STYLE GUIDE (read this first in every new session)

**Book:** *Operator Algebras, Modular Theory, and Quantum Gravity: A Physicist's Guide*
**Reader:** graduate-level physics (QM, QFT, some stat mech/GR), NO formal analysis/topology.
**Goal:** reader can follow Witten's crossed-product paper and CLPW (de Sitter algebra of observables).
Fast track = chapters marked `core` in scripts/chapters.tsv; `skip` = skippable on first read.

## Chapter template (every chapter)
1. `\chapter{..}\label{ch:slug}`; one-paragraph `physmotiv` box FIRST (physics before math).
2. Sections: definition -> worked example -> theorem (proofs sketched via `proofsketch`, full proofs only if illuminating).
3. At least one `whatwrong` box ("What could go wrong").
4. `keyidea` box summarising the chapter's takeaway near the end.
5. `\section*{Exercises}` with 4-8 `exercise` items (mix of computation and conceptual).
6. Forward/back references with `\cref{ch:slug}`. Use the slug in chapters.tsv.
7. End of each Part: a `dictbox` in `parts/partX_dictionary.tex` (physics <-> math dictionary).

## Tone
Physicist-to-physicist. Motivate with finite-dim QM / stat mech first. State precisely what is
true, flag what is only heuristic. No false rigor, no hand-waving that is wrong.
Fast-moving literature (Ch 37-39, 52, parts VII/VIII): use the `unsettled` box and cite carefully.

## Honesty rules
* Never invent citations. If unsure of a reference, use `note={VERIFY}` in refs.bib and flag it in text only via \cite.
* Anything stated from memory about recent papers (2022+) must be re-verified (web search) before finalising.
* Mark conjectural/speculative material explicitly.

## Notation (macros.tex; do not redefine ad hoc)
Hilbert space \HH, bounded ops \BH, algebras \A (C*) \M \N (vN), commutant \comm{\M} = M', bicommutant \bicomm{\M},
centre \cZ, trace \Tr, identity \id, adjoint X^* (use ^*), modular op \Delta, conj. \J (use J), modular flow \sigma_t,
modular Hamiltonian K or K_\psi, crossed product \cp (\rtimes), generalized entropy \Sgen.
Convention: inner product linear in 2nd slot (physics). States: omega or psi; vector states omega_\xi.
Units hbar = c = k_B = 1; G explicit when relevant.

## Conventions on modular theory (FIX NOW, keep forever)
Modular operator Delta_Omega for cyclic separating Omega: S A Omega = A^* Omega, S = J Delta^{1/2}.
Modular flow sigma_t(a) = Delta^{it} a Delta^{-it}.  Modular Hamiltonian: Delta = e^{-K}.
Gibbs state rho = e^{-beta H}/Z  <=>  Delta = rho (x) rho'^{-1}, K = -log rho + log rho'. KMS at beta = -1 for sigma_t.

## Crossed product conventions (LOCKED; derived and checked in finite dimensions, Ch 22-25)
H (x) L^2(R), x position, p = -i d/dx ([x,p]=i). K = -log Delta (K Omega = 0), sigma_t = Ad e^{-itK}.
Frame 1: N = M x|_sigma R = { a (x) 1, X = K + x }''.  Ad e^{-itX} = sigma_t on M, so the flow is INNER in N.
Dual action theta_s = Ad e^{isp}: fixes M, X -> X + s.  M = N^theta.
Dual weight phihat = omega o T (T = Fourier-zero-mode projection); trace tau(b) = phihat(e^{X/2} b e^{X/2}).
tau(f(X)) = int dX e^{X} f(X);  tau o theta_s = e^{-s} tau;  tau(1) = infinity (II_infty).
Frame 2 (physics, CLPW): conjugate by e^{-ipK}:  N ~ { sigma_p(a) = e^{-ipK} a e^{ipK}, x }''.
Constraint generator K - x on M (x) B(L^2): N = invariants of alpha_t = sigma_t (x) Ad e^{itx}.
dS identification: K = beta H, x = -beta q (q = observer energy >= 0), constraint H + q. q >= 0  <=>  x <= 0.
II_1 corner: P = chi(X <= 0), tau(P) = 1. Max-entropy state has density matrix P (S = 0).
Commutant (frame 1): N' = { e^{ipK} a' e^{-ipK} (a' in M'), x }''.

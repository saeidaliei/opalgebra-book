#!/usr/bin/env python3
"""Check of the CLPW entropy formula (CLPW eq. 3.18, book Ch 36) for a GENERAL Phi.

Finite-dimensional model (type I, so everything is exact):
  H = C^n (x) C^n, M = M_n (x) 1,  Omega = sum_i sqrt(p_i)|i,i>,
  K = K_M - K_M',  K|a,j> = (-log p_a + log p_j)|a,j>,   X = K + x on H (x) L^2(R_x).
  N = {M, X}'' = M_n (x) L^inf(R_y),  y = X - K_M = x + log p_j  (acts as x + log p_j on |a,j>).
  Trace: tau(F) = int dy e^y Tr_A F(y)   (Ch 24; tau(f(X)) = int dX e^X f(X) since sum p_i = 1).
State  Phi_hat = Phi (x) g^{1/2}(x),  Phi = sum c_{aj}|a,j>  (arbitrary unit vector).
Exact density matrix (n x n for every y):
  rho_hat(y) = e^{-y} sum_j g(y - log p_j) |c_j><c_j|,   c_j = column j of c.
Exact entropy: S = - int dy e^y Tr[rho_hat log rho_hat].
CLPW formula (their 3.18, in book conventions x = beta*x_CLPW):
  S_CLPW = h(g) + <x>_g + <Phi|K|Phi> - S_rel(Phi||Omega; M)
For Phi = u Omega this is exact (Ch 24).  For general Phi it is the leading term of an expansion in
the inverse width of g (CLPW: O(eps) corrections).  We test that S_exact - S_CLPW -> 0 as width grows.
"""
import numpy as np

rng = np.random.default_rng(7)

def logm_psd(R):
    w, V = np.linalg.eigh(R)
    w = np.clip(w, 1e-300, None)
    return (V * np.log(w)) @ V.conj().T

def exact_entropy(c, p, gfun, lo, hi, N=200001):
    n = len(p)
    y = np.linspace(lo, hi, N); dy = y[1] - y[0]
    cols = [c[:, j] for j in range(n)]
    S = 0.0; norm = 0.0
    # build rho_hat(y) as (N,n,n)
    R = np.zeros((N, n, n), dtype=complex)
    for j in range(n):
        gj = gfun(y - np.log(p[j]))
        R += (np.exp(-y)[:, None, None] * gj[:, None, None]) * np.outer(cols[j], cols[j].conj())[None]
    w = np.linalg.eigvalsh(R)
    w = np.clip(w, 0, None)
    e = np.exp(y)[:, None]
    norm = np.sum(e * w) * dy
    m = w > 1e-300
    integrand = np.where(m, -e * w * np.log(np.where(m, w, 1.0)), 0.0)
    S = np.sum(integrand) * dy
    return S, norm

def clpw_formula(c, p, gfun, lo, hi, N=400001):
    n = len(p)
    x = np.linspace(lo, hi, N); dx = x[1] - x[0]
    G = gfun(x); m = G > 1e-300
    h = -np.sum(G[m] * np.log(G[m])) * dx
    xm = np.sum(x * G) * dx
    rhoA = c @ c.conj().T            # reduced density on A index
    rhoB = (c.T @ c.conj())          # reduced density on B index (transpose convention irrelevant for diag)
    # <K> = sum_a (rhoA)_aa (-log p_a) + sum_j (rhoB)_jj log p_j
    K = -np.sum(np.real(np.diag(rhoA)) * np.log(p)) + np.sum(np.real(np.diag(rhoB)) * np.log(p))
    # Araki relative entropy of Phi to Omega on M_n: Tr rhoA (log rhoA - log diag(p))
    Srel = np.real(np.trace(rhoA @ (logm_psd(rhoA) - np.diag(np.log(p)))))
    return h + xm + K - Srel, h, xm, K, Srel

def random_state(n, kind):
    p = rng.dirichlet(np.ones(n))
    if kind == "uOmega":
        Z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
        u, _ = np.linalg.qr(Z)
        c = u @ np.diag(np.sqrt(p))           # Phi = (u (x) 1) Omega
    else:
        c = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
        c /= np.linalg.norm(c)
    return p, c

if __name__ == "__main__":
    n = 3
    for kind in ("uOmega", "general"):
        p, c = random_state(n, kind)
        print(f"\n=== Phi of kind '{kind}', p = {np.round(p, 3)} ===")
        print(f"{'width s':>8} {'S_exact':>12} {'S_CLPW':>12} {'diff':>12} {'norm':>9}")
        for s in (0.5, 1, 2, 4, 8, 16, 32):
            mu = -10 * s
            gfun = lambda x, mu=mu, s=s: np.exp(-(x - mu) ** 2 / (2 * s * s)) / np.sqrt(2 * np.pi * s * s)
            lo, hi = mu - 12 * s, mu + 12 * s
            Se, nm = exact_entropy(c, p, gfun, lo, hi)
            Sf, *_ = clpw_formula(c, p, gfun, lo, hi)
            print(f"{s:8.1f} {Se:12.6f} {Sf:12.6f} {Se - Sf:12.2e} {nm:9.5f}")

#!/usr/bin/env python3
"""Numerical check of the finite-dimensional crossed-product entropy formula (Ch 24).
State: Omega (x) g^{1/2}(x) on N = M_n (x) L^inf(R_y), y = X + log rho, tau(F)=int dy e^y Tr F(y).
Density matrix eigenvalues: rho_i(y) = e^{-y} p_i g(y - log p_i).
Claim: S = -tau(rho log rho) = <x>_g - int g log g   (independent of p).  Max entropy: g = e^x theta(-x) -> S = 0."""
import numpy as np
def entropy(p, g, lo=-40, hi=40, N=400001):
    y=np.linspace(lo,hi,N); dy=y[1]-y[0]; S=0.0; norm=0.0
    for pi in p:
        r=np.exp(-y)*pi*g(y-np.log(pi))
        w=np.exp(y)
        norm+=np.sum(w*r)*dy
        m=r>1e-300
        S+=-np.sum(w[m]*r[m]*np.log(r[m]))*dy
    return S,norm
def formula(g,lo=-40,hi=40,N=400001):
    x=np.linspace(lo,hi,N); dx=x[1]-x[0]; G=g(x); m=G>1e-300
    return np.sum(x*G)*dx - np.sum(G[m]*np.log(G[m]))*dx
gauss=lambda mu,s: (lambda x: np.exp(-(x-mu)**2/(2*s*s))/np.sqrt(2*np.pi*s*s))
for p in ([0.5,0.5],[0.9,0.1],[0.6,0.3,0.1]):
    for mu,s in ((0,1),(-3,0.5),(2,2)):
        g=gauss(mu,s); S,nm=entropy(p,g)
        print(f"p={p} g=N({mu},{s}) norm={nm:.6f} S={S:.6f} formula={formula(g):.6f}")
gmax=lambda x: np.where(x<=0,np.exp(x),0.0)
for p in ([0.5,0.5],[0.9,0.1]):
    S,nm=entropy(p,gmax,N=800001); print("gmax",p,"norm",round(nm,5),"S",round(S,5),"formula",round(formula(gmax,N=800001),5))

import sympy as sp

zeta = sp.Symbol("\zeta")
eta = sp.Symbol("\eta")
mu = sp.Symbol("\mu")

d_1 = sp.sqrt((zeta + mu) ** 2 + eta ** 2)
d_2 = sp.sqrt((zeta - 1 + mu) ** 2 + eta ** 2)

V = (eta ** 2 + zeta ** 2) / 2 + (1 - mu) / d_1 + mu / d_2

print(sp.latex(sp.diff(V, eta)))
print()
print(sp.latex(sp.diff(V, zeta)))
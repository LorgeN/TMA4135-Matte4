import numpy as np
from sympy.abc import x
from sympy import integrate


def QR(f, xq, wq):
    """Computes an approximation of the integral f
    for a given quadrature rule.

    Input:
        f:  integrand
        xq: quadrature nodes
        wq: quadrature weights
    """
    n = len(xq)
    if n != len(wq):
        raise RuntimeError("Error: Need same number of quadrature nodes and weights!")
    return np.array(wq) @ f(np.array(xq))


for n in range(6):
    print("===========================================")
    print(f"Testing degree of exactness for n = {n}")

    # Define function
    def f(x):
        return x ** n

    # Exact integral
    int_f = integrate(x ** n, (x, -2, 1))

    print("-------------------------------------------")
    print("Testing")

    xq = [-1.662, -0.5, 0.662]
    wq = [0.833, 1.333, 0.833]

    qr_f = QR(f, xq, wq)
    print(f"Q[f] = {qr_f}")
    print(f"I[f] - Q[f] = {int_f - qr_f:.16e}")

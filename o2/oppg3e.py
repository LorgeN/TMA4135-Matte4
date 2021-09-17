from sympy import sqrt, cos, pi, integrate
from sympy.abc import x

BASE_XS = [-sqrt(3 / 5), 0, sqrt(3 / 5)]
BASE_WS = [5 / 9, 8 / 9, 5 / 9]


def __gauss_legendre_quad_part(f, a, b):
    # Adjust for given interval
    xs = (((b - a) * x_i) / 2 + (b + a) / 2 for x_i in BASE_XS)
    ws = ((b - a) * w / 2 for w in BASE_WS)

    return sum(w * f.subs(x, x_i).evalf() for x_i, w in zip(xs, ws))


def gauss_legendre_quad(f, a, b, m):
    h = (b - a) / m
    xs = [a + h * i for i in range(m + 1)]

    return sum(__gauss_legendre_quad_part(f, xs[i], xs[i + 1]) for i in range(m))

if __name__ == "__main__":
    error_est = 1.32 * 10 ** -7

    a = 0
    b = 1

    f = cos(pi * x / 2)

    expect = integrate(f, (x, a, b))
    gl_est = gauss_legendre_quad(f, a, b, 2)

    print(f"Expected: {expect}")
    print(f"Estimate: {gl_est}")
    print(f"Error: {(gl_est - expect).evalf()}, expected error: {error_est}")

from oppg2c import f
from math import cos, pi


def newton(f, df, x0, tol, max_iter=50):
    x = x0

    for k in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            break
        x = x - fx / df(x)
        print(f"{k} & {x:.3f} & {f(x):.3f} \\\\")
    return x


def g(x):
    return x - f(x)


def dg(x):
    return 1 + cos(x)


if __name__ == "__main__":
    x0 = pi / 4
    print(f" x = {newton(g, dg, x0, 0, max_iter=5)}")

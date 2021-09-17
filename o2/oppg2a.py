from sympy.abc import x
from sympy import integrate, sqrt, latex
from functools import lru_cache


def phi(i):
    return x ** i


def scp(p, q, a, b):
    return integrate(p * q, (x, a, b))


def norm(p, a, b):
    return sqrt(integrate(p ** 2, (x, a, b)))


@lru_cache
def p(k, a, b):
    return phi(k) - sum(
        (scp(phi(k), p(j, a, b), a, b) / (norm(p(j, a, b), a, b) ** 2)) * p(j, a, b)
        for j in range(k)
    )


def pretty_p(k, a, b):
    print(
        f"$$\\langle \phi_{k}, p_{k - 1} \\rangle = \\int^{{{b}}}_{{{a}}} \phi_{k}(x)p_{k - 1}(x)dx = {latex(scp(phi(k), p(k - 1, a, b), a, b))}$$"
    )

    print(
        f"$$||p_{k - 1}||^2 = \\int^{{{b}}}_{{{a}}} p_{0}(x)^2 dx = \\int^{{{b}}}_{{{a}}} {latex(p(k - 1, a, b) ** 2)} dx = {latex(norm(p(k - 1, a, b), a, b) ** 2)}$$"
    )

    print(f"$$p_{k} = \phi_{k}", end="")

    for j in range(k):
        print(
            f" - \\frac{{\\langle \phi_{k}, p_{j} \\rangle}}{{||p_{j}||^2}}p_{j}",
            end="",
        )

    print(" = $$")
    print(f"$$ = {latex(phi(k))}", end="")

    for j in range(k):
        print(
            f" - \\frac{{{latex(scp(phi(k), p(j, a, b), a, b))}}}{{{latex(norm(p(j, a, b), a, b) ** 2)}}}{latex(p(j, a, b))}",
            end="",
        )

    print(" = $$")
    print(f"$$ = {latex(p(k, a, b))}$$")
    print()


if __name__ == "__main__":
    a = -2
    b = 1

    for k in range(1, 4):
        pretty_p(k, a, b)

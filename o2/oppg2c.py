from oppg2a import p
from sympy import solve, latex
from sympy.abc import x

if __name__ == "__main__":
    a = -2
    b = 1

    p_3 = p(3, a, b)

    print(latex(solve(p_3, x)))
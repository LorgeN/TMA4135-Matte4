from math import sqrt

from sympy.abc import W

if __name__ == "__main__":
    a = -2
    b = 1

    xs = [-sqrt(3 / 5), 0, sqrt(3 / 5)]
    x_vals = ", ".join(str(round(((b - a) * x) / 2 + (b + a) / 2, 3)) for x in xs)
    print(f"${x_vals}$")

    ws = [5/9, 8/9, 5/9]
    w_vals = ", ".join(str(round((b - a) * w / 2, 3)) for w in ws)
    print(f"${w_vals}$")

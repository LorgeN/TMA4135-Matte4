import matplotlib.pyplot as plt
from oppg1b import composite_simpson, plot_eoc
from math import pi, sqrt

if __name__ == "__main__":
    def func(x):
        return sqrt(1 - x ** 2)

    expected = pi / 4

    a = 0
    b = 1
    ms = [4, 8, 16, 32, 64]

    t_errs = []
    t_hs = []

    s_errs = []
    s_hs = []

    for m in ms:
        approx = composite_simpson(func, a, b, m)
        s_errs.append(abs(approx - expected))
        s_hs.append((b - a) / m)

    print("Simpsons")
    plot_eoc(s_hs, s_errs)

    plt.legend(["Simpsons"])
    plt.xlabel("log(h)")
    plt.ylabel("log(err)")
    plt.show()
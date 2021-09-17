import numpy as np
import matplotlib.pyplot as plt
from math import tan, log, pi

newparams = {
    "figure.figsize": (8.0, 4.0),
    "axes.grid": True,
    "lines.markersize": 8,
    "lines.linewidth": 2,
    "font.size": 14,
}
plt.rcParams.update(newparams)


def composite_simpson(f, a, b, m):
    h = (b - a) / m

    total = 0

    xs = [a + (h * i) for i in range(m + 1)]

    for i in range(1, m + 1):
        total += f(xs[i - 1]) + 4 * f((xs[i - 1] + xs[i]) / 2) + f(xs[i])

    return (h / 6) * total


def composite_trapezoid(f, a, b, m):
    h = (b - a) / m
    xs = [a + (h * i) for i in range(m + 1)]
    return h * (0.5 * f(xs[0]) + 0.5 * f(xs[-1]) + sum(f(x) for x in xs[1:-1:]))


def plot_eoc(hs, errs):
    # Shamelessly stolen from handout
    hs = np.array(hs)
    errs = np.array(errs)

    eocs = np.log(errs[1:] / errs[:-1]) / np.log(hs[1:] / hs[:-1])
    eocs = np.insert(eocs, 0, np.inf)

    print("".ljust(10) + "Error:".ljust(30) + "EOC:".ljust(30))
    for i, err, eoc in zip(range(len(errs)), errs, eocs):
        print(f"{i} & ".ljust(10) + f"{err} & ".ljust(30) + f"{eoc} \\\\ ")

    plt.loglog(hs, errs, "o-")


if __name__ == "__main__":

    def func(x):
        return tan((pi / 4) * x)

    expected = 2 * log(2) / pi

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

        approx = composite_trapezoid(func, a, b, m)
        t_errs.append(abs(approx - expected))
        t_hs.append((b - a) / m)

    print("Trapezoid")
    plot_eoc(t_hs, t_errs)
    print("Simpsons")
    plot_eoc(s_hs, s_errs)

    plt.legend(["Trapezoid", "Simpsons"])
    plt.xlabel("log(h)")
    plt.ylabel("log(err)")
    plt.show()

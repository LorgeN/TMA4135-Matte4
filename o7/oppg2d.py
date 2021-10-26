from oppg2b import *
from oppg1b import fb_rk as rk
import matplotlib.pyplot as plt


def run(deta0):
    y0 = np.array([0.994, 0, 0, deta0])
    t0 = 0
    T = 20
    Nmax = 1000
    Tol = 10 ** -6

    plt.figure()
    ts, ys = rk(y0, t0, T, f, Nmax, Tol)

    t_diffs = np.abs(np.diff(ts))

    min_step = t_diffs.min()
    max_step = t_diffs.max()

    print(f"Max step: {max_step:.4f}, min step: {min_step:.4f}, ratio: {max_step/min_step:.4f}")

    plt.plot(earth[0], earth[1], "go", markersize="20")
    plt.plot(moon[0], moon[1], "ro", markersize="10")
    plt.ylabel("$\\eta$")
    plt.xlabel("$\\zeta$")
    plt.plot(ys[:, 0], ys[:, 1])
    plt.show()


if __name__ == "__main__":
    for deta in [-2.0317326, -2.0015851, -2.1]:
        print()
        run(deta)

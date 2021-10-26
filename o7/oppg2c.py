from oppg2b import *
from oppg1a import EmbeddedExplicitRungeKutta
import matplotlib.pyplot as plt

a = np.array([[0, 0, 0, 0], [1 / 2, 0, 0, 0], [0, 1 / 2, 0, 0], [0, 0, 1, 0]])
b = np.array([1 / 6, 1 / 3, 1 / 3, 1 / 6])
c = np.array([0, 1 / 2, 1 / 2, 1])

rk = EmbeddedExplicitRungeKutta(a, b, c, None, 4)


def run(deta0):
    y0 = np.array([0.994, 0, 0, deta0])
    t0 = 0
    T = 20
    Nmax = 10000

    plt.figure()
    ts, ys = rk(y0, t0, T, f, Nmax, None)
    plt.plot(earth[0], earth[1], "go", markersize="20")
    plt.plot(moon[0], moon[1], "ro", markersize="10")
    plt.ylabel("$\\eta$")
    plt.xlabel("$\\zeta$")
    plt.plot(ys[:, 0], ys[:, 1])
    plt.show()


if __name__ == "__main__":
    for deta in [-2.0317326, -2.0015851, -2.1]:
        run(deta)

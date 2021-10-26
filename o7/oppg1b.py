from oppg1a import EmbeddedExplicitRungeKutta
import numpy as np
import matplotlib.pyplot as plt

LAMBDA = 1
Y0 = 1
T0 = 0
T = 1
tol = 10 ** -3
Nmax = 100


def f_1(t, y):
    return LAMBDA * y


def y_1(t):
    return Y0 * np.e ** (LAMBDA * (t - T0))


def f_2(t, y):
    return -2 * t * y


def y_2(t):
    return np.e ** (-(t ** 2))


eh_a = np.array([[0, 0], [1, 0]])
eh_b = np.array([1 / 2, 1 / 2])
eh_c = np.array([0, 1])
eh_bhat = np.array([1, 0])

eh_rk = EmbeddedExplicitRungeKutta(eh_a, eh_b, eh_c, eh_bhat, 1)

fb_a = np.array(
    [
        [0, 0, 0, 0, 0, 0],
        [1 / 4, 0, 0, 0, 0, 0],
        [3 / 32, 9 / 32, 0, 0, 0, 0],
        [1932 / 2197, -7200 / 2197, 7296 / 2197, 0, 0, 0],
        [439 / 216, -8, 3680 / 513, -845 / 4104, 0, 0],
        [-8 / 27, 2, -3544 / 2565, 1859 / 4104, -11 / 40, 0],
    ]
)
fb_b = np.array([16 / 135, 0, 6656 / 12825, 28561 / 56430, -9 / 50, 2 / 55])
fb_c = np.array([0, 1 / 4, 3 / 8, 12 / 13, 1, 1 / 2])
fb_bhat = np.array([25 / 216, 0, 1408 / 2565, 2197 / 4104, -1 / 5, 0])

fb_rk = EmbeddedExplicitRungeKutta(fb_a, fb_b, fb_c, fb_bhat, 4)


def run_and_plot(rk, f, y):
    ts, ys = rk(Y0, T0, T, f, Nmax, tol)
    plt.plot(ts, ys, label="RK")

    actual_t = np.arange(T0, T, 0.01)
    actual_ys = y(actual_t)
    plt.plot(actual_t, actual_ys, label="Actual")

    plt.legend()
    plt.show()


if __name__ == "__main__":
    print("\nEuler Heun 1")
    run_and_plot(eh_rk, f_1, y_1)
    print("\nEuler Heun 2")
    run_and_plot(eh_rk, f_2, y_2)

    print("\nFehlberg 1")
    run_and_plot(fb_rk, f_1, y_1)
    print("\nFehlberg 2")
    run_and_plot(fb_rk, f_2, y_2)

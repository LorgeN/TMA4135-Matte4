from oppg2a import explicit_mid_point_rule, ssprk3
import numpy as np
import matplotlib.pyplot as plt


def f(t, y):
    return -2 * t * y


def y(t):
    return np.e ** (-(t ** 2))


if __name__ == "__main__":
    t0 = 0
    T = 0.5
    y0 = 1

    mp_ts, mp_ys = explicit_mid_point_rule(y0, t0, T, f, 3)
    plt.plot(mp_ts, mp_ys, label="Midpoint Rule")

    ss_ts, ss_ys = ssprk3(y0, t0, T, f, 2)
    plt.plot(ss_ts, ss_ys, label="SSPRK3")

    actual_t = np.arange(t0, T, 0.01)
    actual_ys = y(actual_t)
    plt.plot(actual_t, actual_ys, label="Actual")
    plt.legend()
    plt.show()

    mp_err = np.abs(y(0.5) - mp_ys[-1])
    ss_err = np.abs(y(0.5) - ss_ys[-1])

    print(f"Errors: Midpoint rule: {mp_err:.5f}, SSRPK3: {ss_err:.5f}")

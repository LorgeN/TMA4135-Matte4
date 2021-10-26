import matplotlib.pyplot as plt
import numpy as np


def base_rk(y0, t0, T, f, max_steps, a, b, c):
    tau = (T - t0) / max_steps

    ts = [t0]
    ys = [y0]

    s = len(a)

    while ts[-1] < T:
        t_k, y_k = ts[-1], ys[-1]

        y_tmp = []
        for j in range(s):
            yj_sum_part = sum(
                a[j][l] * f(t_k + c[l] * tau, y_tmp[l]) for l in range(s) if a[j][l]
            )
            y_tmp.append(y_k + tau * yj_sum_part)

        yk1_sum = sum(b[j] * f(t_k + c[j] * tau, y_tmp[j]) for j in range(s))
        ys.append(y_k + tau * yk1_sum)
        ts.append(t_k + tau)

    return ts, ys


def explicit_mid_point_rule(y0, t0, T, f, max_steps):
    a = [[0, 0], [1 / 2, 0]]
    b = [0, 1]
    c = [0, 1 / 2]

    return base_rk(y0, t0, T, f, max_steps, a, b, c)


def ssprk3(y0, t0, T, f, max_steps):
    a = [[0, 0, 0], [1, 0, 0], [1 / 4, 1 / 4, 0]]
    b = [1 / 6, 1 / 6, 2 / 3]
    c = [0, 1, 1 / 2]

    return base_rk(y0, t0, T, f, max_steps, a, b, c)


def f(t, y):
    return -y


if __name__ == "__main__":
    t0 = 0
    T = 10
    y0 = 1
    steps = 10

    mp_ts, mp_ys = explicit_mid_point_rule(y0, t0, T, f, steps)
    plt.plot(mp_ts, mp_ys, label="Midpoint Rule")

    ss_ts, ss_ys = ssprk3(y0, t0, T, f, steps)
    plt.plot(ss_ts, ss_ys, label="SSPRK3")

    actual_t = np.arange(t0, T, 0.05)
    actual_ys = np.e ** (-actual_t)
    plt.plot(actual_t, actual_ys, label="Actual")
    plt.legend()
    plt.show()

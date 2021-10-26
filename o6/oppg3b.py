from oppg2a import ssprk3
import numpy as np
import matplotlib.pyplot as plt

beta = 0.2
gamma = 0.15


def f(t, y):
    return np.array(
        [-beta * y[0] * y[1], beta * y[0] * y[1] - gamma * y[1], gamma * y[1]]
    )


if __name__ == "__main__":
    t0 = 0
    T = 50
    y0 = np.array([50, 10, 0])
    steps = 500

    ts, ys = ssprk3(y0, t0, T, f, steps)

    ys = np.array(ys)

    S = ys[:, 0]
    I = ys[:, 1]
    R = ys[:, 2]

    plt.plot(ts, S, label="Susceptible")
    plt.plot(ts, I, label="Infected")
    plt.plot(ts, R, label="Recovered")
    plt.plot(ts, S + I + R, label="Total")
    plt.legend()
    plt.show()

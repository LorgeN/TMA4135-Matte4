from oppg2a import explicit_mid_point_rule, ssprk3, f
import numpy as np


def y(t):
    return np.e ** -t


def estimate_eoc(method):
    t0 = 0
    T = 10
    y0 = 1

    error = []
    taus = []

    for m in range(6):
        tau = 2 ** -m
        steps = np.ceil((T - t0) / tau)

        _, ys = method(y0, t0, T, f, steps)

        error.append(np.abs(y(T) - ys[-1]))
        taus.append(tau)

    return [
        np.log(error[m] / error[m + 1]) / np.log(taus[m] / taus[m + 1])
        for m in range(5)
    ]


def format_eoc(name, eocs):
    print(f"EOC estimates for {name}: ")
    print(", ".join(str(round(eoc, 2)) for eoc in eocs))
    print(f" Average: {np.average(eocs):.2f}")


if __name__ == "__main__":
    format_eoc("Midpoint Rule", estimate_eoc(explicit_mid_point_rule))
    format_eoc("SSPRK3", estimate_eoc(ssprk3))

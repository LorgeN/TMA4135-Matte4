import numpy as np
from math import cos, pi


def chebyshev_nodes(a, b, n):
    i = np.arange(n)
    x_i = np.cos((2 * i + 1) * np.pi / (2 * n))
    return ((b - a) / 2) * x_i + (b + a) / 2


if __name__ == "__main__":
    for i, v in enumerate(chebyshev_nodes(2, 5, 4)):
        print(f"{i}: {v}")

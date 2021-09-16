import numpy as np
from functools import lru_cache
from numpy.polynomial.polynomial import Polynomial


def get_w_values(x_values):
    if not len(x_values):
        return []

    polys = [Polynomial([1])]

    for i, x_i in enumerate(x_values[:-1]):
        polys.append(polys[i] * Polynomial([-x_i, 1]))

    return polys


# Will memoize our function for some more speedy operations
# when doing the same calls many times
@lru_cache
def dd(x_val, y_val, indices):
    if len(indices) == 1:
        return y_val[indices[0]]

    dd_1 = dd(x_val, y_val, indices[1:])
    dd_2 = dd(x_val, y_val, indices[:-1])
    divisor = x_val[indices[-1]] - x_val[indices[0]]
    return (dd_1 - dd_2) / divisor


def interpolate(x_val, y_val):
    w = get_w_values(x_val)

    result = Polynomial([0])

    for k in range(len(x_val)):
        result += dd(x_val, y_val, tuple(range(0, k + 1))) * w[k]

    return result


def verify(x_val, y_val, result):
    res_val = result(np.array(x_val))

    print("X:".ljust(20) + "Interp:".ljust(20) + "Error:")
    for x, actual, expected in zip(x_val, res_val, y_val):
        diff = actual - expected
        print(str(x).ljust(20) + str(actual).ljust(20) + str(diff))

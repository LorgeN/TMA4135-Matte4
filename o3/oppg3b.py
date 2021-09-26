from oppg2d import newton
from math import log


def f(x):
    return log(x) - 1


def df(x):
    return 1 / x


if __name__ == "__main__":
    x0 = 3
    print(f" x = {newton(f, df, x0, 0, max_iter=2)}")

def bisect(f, a, b, err):
    c = (a + b) / 2
    if (b - a) <= 2 * err:
        return c

    f_c = f(c)
    f_a = f(a)
    if (f_a > 0 and f_c < 0) or (f_a < 0 and f_c > 0):
        return bisect(f, a, c, err)
    return bisect(f, c, b, err)


def f(x):
    return 4 * x ** 3 - 3 * x ** 2 + 8 * x - 12


if __name__ == "__main__":
    error = 1 / 32
    val = bisect(f, 0, 2, error)
    print(f"[{val - error}, {val + error}]")

from math import sin, pi


def fixed_point_iter(f, x0, tol, max_iter=50):
    x = x0

    for i in range(max_iter):
        x_prev = x
        x = f(x)
        err = abs(x - x_prev)

        print(f" {i} & {x:.3f} & {err:.3f} \\\\")
        i += 1
        if err < tol:
            break

    return x


def f(x):
    return 1 - sin(x)


if __name__ == "__main__":
    x0 = pi / 4
    print(f" x = {fixed_point_iter(f, x0, 0, max_iter=5)}")

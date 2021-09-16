from interpolate_newton import interpolate, verify
from oppg4a import chebyshev_nodes


def f(x):
    return 2 ** (x ** 2 - 6 * x + 9)


x_val = tuple(chebyshev_nodes(2, 5, 4))
y_val = tuple(f(x) for x in x_val)

poly = interpolate(x_val, y_val)

print(f"{poly:ascii}")
verify(x_val, y_val, poly)

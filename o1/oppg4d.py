from interpolate_newton import interpolate, verify
from oppg4a import chebyshev_nodes
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 2 ** (x ** 2 - 6 * x + 9)

def make_cheby():
    x_val = tuple(chebyshev_nodes(2, 5, 4))
    plt.title("Chebyshev")
    plot_diffs(x_val)

def make_uniform():
    x_val = tuple(range(2, 6, 1))
    plt.title("Uniform")
    plot_diffs(x_val)
    

def plot_diffs(x_val):
    y_val = tuple(f(x) for x in x_val)

    poly = interpolate(x_val, y_val)

    xs = np.linspace(2, 5, 100)
    eval_poly = poly(xs)
    eval_f = np.vectorize(f)(xs)

    plt.subplot(2, 1, 1)
    plt.plot(xs, eval_poly)
    plt.plot(xs, eval_f)
    plt.plot(x_val, y_val, 'o')
    plt.legend(["p(x)", "f(x)", "Points"])
    plt.grid(True)

    error = eval_poly - eval_f

    plt.subplot(2, 1, 2)
    plt.plot(xs, error)
    plt.legend(["Error"])
    plt.grid(True)

    print(f"Max error is {max(abs(error)):.3f}")

    plt.show()

make_uniform()
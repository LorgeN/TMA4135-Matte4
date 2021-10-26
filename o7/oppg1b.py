from oppg1a import EmbeddedExplicitRungeKutta
import numpy as np

LAMBDA = 1
Y0 = 1
T0 = 0

def f(t, y):
    return LAMBDA * y

def y(t):
    return Y0 * np.e ** (LAMBDA * (t - T0))

def euler_heun(f, y):
    a = np.array([[0, 0], [1, 0]])  
    b = np.array([1/2, 1/2])
    c = np.array([0, 1])
    bhat = np.array([1, 0])

    rk = EmbeddedExplicitRungeKutta(a, b, c, bhat, 1)

    T = 1
    tol = 10 ** -3
    Nmax = 100

    # y0, t0, T, f, Nmax, tol
    ts, ys = rk(Y0, T0, T, f, Nmax, tol)

    print(f"Error: {ys[-1] - y(T)}")

if __name__ == "__main__":
    
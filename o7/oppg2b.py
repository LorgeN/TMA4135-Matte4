import numpy as np

# Parameters for the system
mu = 0.012277471
earth = np.array([-mu, 0])
moon = np.array([1 - mu, 0])

# Force field to be solved
def f(t, y):
    # y = (xi,eta,xi_prime,eta_prime)
    xi, eta, xi_prime, eta_prime = y

    # the distances can be computed using linalg in numpy
    d1 = np.linalg.norm(y[0:2] - earth, 2)
    d2 = np.linalg.norm(y[0:2] - moon, 2)

    # the vector of derivatives
    dy1 = xi_prime
    dy2 = eta_prime

    dy3 = 2 * dy2 + xi + mu * (-mu - xi + 1) / d2 ** 3 + (1 - mu) * (-mu - xi) / d1 ** 3
    dy4 = -2 * dy1 + eta - (eta * mu) / d2 ** 3 - eta * (1 - mu) / d1 ** 3 
    return np.array([dy1, dy2, dy3, dy4])

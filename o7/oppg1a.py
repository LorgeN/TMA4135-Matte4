import numpy as np
from numpy.linalg import norm, solve
import matplotlib.pyplot as plt


class EmbeddedExplicitRungeKutta:
    def __init__(self, a, b, c, bhat, order):
        self.a = a
        self.b = b
        self.c = c
        self.bhat = bhat
        self.order = order

    def __call__(self, y0, t0, T, f, Nmax, tol):
        # Stages
        s = len(self.b)
        ks = [np.zeros_like(y0, dtype=np.double) for s in range(s)]

        # Start time-stepping
        ys = [y0]
        ts = [t0]

        dt = (T - t0) / Nmax

        # Counting steps to avoid infinite loops
        N = 0
        N_rej = 0

        while ts[-1] < T and N < Nmax:
            t, y = ts[-1], ys[-1]
            N += 1

            # Compute stages derivatives k_j
            for j in range(s):
                t_j = t + self.c[j] * dt
                dY_j = sum(self.a[j, l] * ks[l] for l in range(j))
                ks[j] = f(t_j, y + dt * dY_j)

            # Compute next time-step
            dy = sum(self.b[i] * ks[i] for i in range(s))

            # If bhat was not given then fall back to a standard RKM with uniform step size
            if self.bhat is None:
                ys.append(y + dt * dy)
                ts.append(t + dt)
            else:
                dyhat = sum(self.bhat[i] * ks[i] for i in range(s))

                # Error estimate
                err = norm(dt * (dyhat - dy))

                # Accept time-step
                if err <= tol:
                    ys.append(y + dt * dyhat)
                    ts.append(t + dt)
                else:
                    #print(f"Step is rejected at t = {t}, N = {N} with err = {err}")
                    N_rej += 1

                dt = dt * 0.8 * (tol / err) ** (1 / (self.order + 1))

        print(f"Finishing time-stepping reaching t = {ts[-1]} with final time T = {T}")
        print(f"Used {N} steps out of {Nmax} with {N_rej} being rejected")

        return (np.array(ts), np.array(ys))

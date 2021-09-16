import numpy as np
from interpolate_newton import interpolate, verify

x_val = (1976, 1981, 1986, 1991, 1996, 2001)
y_val = (4017101, 4092340, 4159187, 4249830, 4369957, 4503436)

poly = interpolate(x_val, y_val) 

eval = np.array([1983, 1999, 2010, 2020])
values = poly(eval)

for x, y in zip(eval, values):
    print(f"{x}: {y}")
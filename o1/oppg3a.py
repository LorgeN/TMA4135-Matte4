from interpolate_newton import interpolate, verify

x_val = (1976, 1981, 1986, 1991, 1996, 2001)
y_val = (4017101, 4092340, 4159187, 4249830, 4369957, 4503436)

poly = interpolate(x_val, y_val) 

print(f"{poly:ascii}")
verify(x_val, y_val, poly)
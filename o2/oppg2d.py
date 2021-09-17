from oppg2a import p
from sympy import solve, latex, expand, integrate
from sympy.abc import x

def lagrange_poly(roots, i):
    tot = None

    for j, root in enumerate(roots):
        if i == j:
            continue
        
        if not tot:
            tot = (x - root) / (roots[i] - root)
        else:
            tot *= (x - root) / (roots[i] - root)
    
    return tot

def pretty_print(roots, i):
    dividend = "".join(f"(x - {root})" for j, root in enumerate(roots) if not i == j)
    divisor = "".join(f"({roots[i]} - {root})" for j, root in enumerate(roots) if not i == j)
    return f"\\frac{{{dividend}}}{{{divisor}}}"

def part_1():
    a = -2
    b = 1

    p_3 = p(3, a, b)

    roots = [round(r.evalf(), 3) for r in solve(p_3, x)]

    print(f"")
    for i in range(len(roots)):
        poly = lagrange_poly(roots, i)
        print(f"$$l_{i + 1} = {pretty_print(roots, i)} = {latex(expand(poly))}$$")
        print()

if __name__ == "__main__":
    a = -2
    b = 1

    p_3 = p(3, a, b)

    roots = [round(r.evalf(), 3) for r in solve(p_3, x)]

    for i in range(len(roots)):
        poly = expand(lagrange_poly(roots, i))
        print(f"$$w_{i + 1} = \\int^{{{b}}}_{{{a}}} ({latex(poly)}) dx = {integrate(poly, (x, a, b))}$$")


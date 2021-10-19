from sympy import Rational, latex

def gen_4_1(a, b, c):
    for i in range(len(c)):
        for j in range(len(b)):
            print(f"{latex(b[i])} * {latex(c[i])} * {latex(a[i][j])} * {latex(c[j])} + ", end="") 
        print("")

    return sum(sum(b[i] * c[i] * a[i][j] * c[j] for j in range(len(b))) for i in range(len(c)))

if __name__ == "__main__":
    c = [0, 1, Rational(1, 2)]
    b = [Rational(1, 6), Rational(1, 6), Rational(2, 3)]
    a = [
        [0, 0, 0],
        [1, 0, 0],
        [Rational(1, 4), Rational(1, 4), 0]
    ]

    print(f" = {latex(gen_4_1(a, b, c))}")
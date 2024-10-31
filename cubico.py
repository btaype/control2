from sympy import Matrix, Rational

A_sympy = Matrix([
    [Rational(1.5**3), Rational(1.5**2), Rational(1.5), 0, 0, 0, 0, 0, 0],
    [0, 0, 0, Rational(2.5**3), Rational(2.5**2), Rational(2.5), 0, 0, 0],
    [0, 0, 0, 0, 0, 0, Rational(2**3), Rational(2**2), Rational(2)],
    [Rational(3 * 1.5**2), Rational(2 * 1.5), 1, 0, 0, -1, 0, 0, 0],
    [0, 0, 0, Rational(3 * 2.5**2), Rational(2 * 2.5), 1, 0, 0, -1],
    [Rational(6 * 1.5), 2, 0, 0, -2, 0, 0, 0, 0],
    [0, 0, 0, Rational(6 * 2.5), 2, 0, 0, -2, 0],
    [0, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 12, 2, 0]
])

b_sympy = Matrix([Rational(-3, 2), Rational(3, 2), Rational(-2), 0, 0, 0, 0, 0, 0])


x_sympy = A_sympy.LUsolve(b_sympy)

import sympy as sp
x = sp.symbols('x')
f = x**2 + 3*x + 2
integral = sp.integrate(f, x)
print(integral)
import sympy as sp
x = sp.symbols('x')
f = sp.exp(x)
integral = sp.integrate(f, x)
print(integral)

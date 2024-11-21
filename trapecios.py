import numpy as np
def trapecios(f, a, b, n):
    h = (b - a) / n
    I = (f(a) + f(b)) / 2
    for k in range(1, n):
        I += f(a + k * h)
    I *= h
    return I
def funcion(x):
    return (5*x + 4) - np.cbrt(x)
def fun2(x):
    return ((16 - x) / 4) - np.cbrt(x)
def funcionTIP2(x):
    return (x**3) - ((x-4)/5)
def fun2TIP2(x):
    return (-4*x+16)-((x-4)/5)
resultado = trapecios(funcion, -1, 0, 50)
resultado2 = trapecios(fun2, 0, 8, 50)
resultadotip2 = trapecios(funcionTIP2, -1, 2, 50)
resultado2tip2 = trapecios(fun2TIP2, 2, 4, 50)
print("AREA TIPO 1:", resultado+resultado2)
print("AREA TIPO 2:", resultadotip2 +resultado2tip2)

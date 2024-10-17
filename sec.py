def secante(f, x0, x1, tolerancia):
    while abs(x1 - x0) > tolerancia:
        f_x0 = f(x0)
        f_x1 = f(x1)
        x_temp = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        x0, x1 = x1, x_temp
    return x1

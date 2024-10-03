def punto_fijo(g, x0, tol, max_iter):
    x_n = x0
    for n in range(max_iter):
        x_n1 = g(x_n) 
        if abs(x_n1 - x_n) < tol:
            print(f"Converged after {n + 1} iterations")
            return x_n1
        x_n = x_n1 

    return None
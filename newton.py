def newton_raphson(f, df, x0, tol, max_iter):
    xn = x0
    for n in range(max_iter):
        fxn = f(xn)        
        dfxn = df(xn)        
        if abs(dfxn) < 1e-10:
            print("La derivada es demasiado pequeña")
            return None
        xn_next = xn - fxn / dfxn  
        if abs(xn_next - xn) < tol:
            print(f"Converged after {n+1} iterations")
            return xn_next
        xn = xn_next  
    print("NO")
    return None
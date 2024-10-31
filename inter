from sympy import *
X=symbols('x')

def lagrange (x1,y):
  d=0
  for i in  range(len(y)):
    t=x1[0:i]+x1[i+1::]
    
    z=1
    for j in range(len(t)):
     
      z=z*((X-t[j])/(x1[i]-t[j]))
    d=d+y[i]*z
  return d
def newton(x1,y1):
  f=y1[0]+X-X
  for i in range(1,len(x1)):
    d=(f.subs(X,x1[i]))
    t=x1[0:i]
   
    d1=prod(X-j for j in (t))
    
    R=(y1[i]-d)/(d1.subs(X,x1[i]))
    
    f=f+R*d1
    
  return f

x = [1, 3, 4]
y = [2, 5, 3]
f = lagrange(x, y)
resultado = f.subs(X, 5)

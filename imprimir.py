import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5, 5, 200)
y = np.piecewise(x, [x < 0, x >= 0], 
                 [lambda x: 5 * np.cos(x**2 - x),  
                  lambda x: x**2 + 3*x + 5])    
plt.plot(x, y)
plt.axhline(0, color='black', linewidth=0.5) 
plt.axvline(0, color='black', linewidth=0.5) 
plt.show()
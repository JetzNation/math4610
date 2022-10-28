**Name:** Andy Skabelund  
**Task 1:** The link to my software manuals can be found at the following address: https://github.com/JetzNation/math4610/tree/main/Software%20Manuals  
My Newton's method code is as follows:  
```
import numpy as np


def f_of_x(x):
    return x * np.exp(-x)


def d_of_x(x):
    return -1 * (x - 1) * np.exp(-x)

def newtonsMethod(func, fderiv, x, maxIter):
    iteration = 0

    while (iteration < maxIter):
        i = x - (f_of_x(x) / d_of_x(x))
        x = i
        iteration += 1
    print(f"The root is found at {x} after {iteration} iterations")

newtonsMethod(f_of_x, d_of_x, .5, 10)
```  
Output:  
```
The root is found at 0.0 after 10 iterations
```  
**Task 2:**  
My Secant method code is as follows:  
```
import numpy as np


def f_of_x(x):
    return x * np.exp(-x)

def secantMethod(func, x0, x1, maxIter):
    iteration = 0

    while (iteration < maxIter):
        fx0 = f_of_x(x0)
        fx1 = f_of_x(x1)

        xi = x0 - (fx0 / (fx0 - fx1))
        x0 = x1
        x1 = xi
        iteration += 1
    print(f"The root is found at {xi} after {iteration} iterations")

secantMethod(f_of_x, 3, -1, 1)
```  
Output:  
```

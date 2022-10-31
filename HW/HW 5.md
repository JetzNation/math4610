**Name:** Andy Skabelund  
**Task 1:** My implicit Euler code is as follows:  
```
import numpy as np
from newton import newtonsMethod

def implicitEuler(f, df, x0, t0, T, n):
    h = (T - t0) / n
    f0 = f(t0, x0)
    tval = []
    xval = []
    tval.append(t0)
    xval.append(x0)
    for i in range(1, n):
        t1 = t0 + h
        x1 = newtonsMethod(lambda x: x - x0 - h * f(t1, x), lambda x: 1 - h * df(t1, x), x0, .00000001, 50)
        x0 = x1
        t0 = t1
        tval.append(t0)
        xval.append(x0)
    return tval, xval
```
    My Newton's method code is:  
```
import numpy as np


def newtonsMethod(func, fderiv, x0, tol, maxIter):
    iteration = 0
    error = 0

    while (iteration < maxIter and tol < error):
        f0 = func(x0)
        df0 = fderiv(x0)
        x1 = x0 - f0 / df0
        error = np.abs(x1 - x0)
        iteration += 1
        x0 = x1
    return x0
```  
    The code to test these is:  
```
import numpy as np
import matplotlib.pyplot as plt
from ImplicitEuler import implicitEuler
from ExplicitEuler import explicitEuler

def logisticEquation(a, b, p0):
    p = lambda t, x: a * x - b * x * x
    tval, pval = explicitEuler(p, p0, 0, 10, 100)
    return tval, pval

tApprox1, xApprox1 = logisticEquation(.2, 0.0005, 10.0)
tApprox2, xApprox2 = logisticEquation(.01, 0.0005, 10.0)
tApprox3, xApprox3 = logisticEquation(2, 0.0005, 10.0)
plt.plot(tApprox1, xApprox1, color="yellow")
plt.xlabel("t")
plt.ylabel("P(t)")
plt.show()
plt.plot(tApprox2, xApprox2, color="orange")
plt.xlabel("t")
plt.ylabel("P(t)")
plt.show()
plt.plot(tApprox3, xApprox3, color="red")
plt.xlabel("t")
plt.ylabel("P(t)")
plt.show()
```  
Output:  
![Figure_1](https://user-images.githubusercontent.com/22015224/199112949-41523939-e84e-4295-bcf8-2316c2239dbc.png)  
![Figure_2](https://user-images.githubusercontent.com/22015224/199113405-b8367bc5-069a-4a4b-a5d2-797ea67e18cd.png)
![Figure_3](https://user-images.githubusercontent.com/22015224/199113089-23a781d6-0a80-49bf-a92c-2591822b8502.png)  
**Task 2:**  
These are the steps that I took to solve the differential equation:  
<img width="475" alt="Screen Shot 2022-10-31 at 12 37 31 PM" src="https://user-images.githubusercontent.com/22015224/199114960-624f5ff8-f077-4399-92b3-f782470cf98d.png">  
then  
<img width="671" alt="Screen Shot 2022-10-31 at 12 38 57 PM" src="https://user-images.githubusercontent.com/22015224/199115833-b6c9d270-b93d-4963-94af-45c6276064c1.png">
The equation is:  
<img width="233" alt="Screen Shot 2022-10-31 at 12 40 25 PM" src="https://user-images.githubusercontent.com/22015224/199117828-6026aa62-458d-49f3-a60d-d0b016616b11.png">
and finally  
<img width="220" alt="Screen Shot 2022-10-31 at 12 41 05 PM" src="https://user-images.githubusercontent.com/22015224/199118076-58da0222-5038-44af-b521-00431d0fe3df.png">
My code for the exact equation is:  
```
import numpy as np
def exactLogistic(a, b, p0, t0, T, n):
    h = T / n
    tval = []
    pval = []
    t0 = 0
    tval.append(t0)
    pval.append(p0)
    for i in range(1, n):
        t1 = t0 + h
        p1 = (a * p0 * np.exp(a * t1)) / (a + b * p0 * (np.exp(a * t1) - 1))
        tval.append(t1)
        pval.append(p1)
        t0 = t1
    return tval, pval
```

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
**Task 3:**  
My code for comparing the equations is:  
```
import numpy as np
import matplotlib.pyplot as plt
from ImplicitEuler import implicitEuler
from ExplicitEuler import explicitEuler
from ExactLogistic import exactLogistic
def logisticEquation(a, b, p0):
    p = lambda t, x: a * x - b * x * x
    dp = lambda t, x: a - 2 * b * x
    tval1, pval1 = explicitEuler(p, p0, 0, 10, 100)
    tval2, pval2 = implicitEuler(p, dp, p0, 0, 10, 100)
    tval3, pval3 = exactLogistic(a, b, p0, 0, 10, 100)
    return tval1, pval1, tval2, pval2, tval3, pval3

tApprox1, xApprox1, tApprox2, xApprox2, tApprox3, xApprox3 = logisticEquation(.2, 0.0005, 10.0)
tApprox4, xApprox4, tApprox5, xApprox5, tApprox6, xApprox6 = logisticEquation(.01, 0.0005, 10.0)
tApprox7, xApprox7, tApprox8, xApprox8, tApprox9, xApprox9 = logisticEquation(2, 0.0005, 10.0)
plt.title("Example 1")
plt.plot(tApprox1, xApprox1, color="yellow")
plt.plot(tApprox2, xApprox2, color="orange")
plt.plot(tApprox3, xApprox3, color="red")
plt.xlabel("t")
plt.ylabel("P(t)")
plt.show()
plt.title("Example 2")
plt.plot(tApprox4, xApprox4, color="yellow")
plt.plot(tApprox5, xApprox5, color="orange")
plt.plot(tApprox6, xApprox6, color="red")
plt.xlabel("t")
plt.ylabel("P(t)")
plt.show()
plt.title("Example 3")
plt.plot(tApprox7, xApprox7, color="yellow")
plt.plot(tApprox8, xApprox8, color="orange")
plt.plot(tApprox9, xApprox9, color="red")
plt.xlabel("t")
plt.ylabel("P(t)")
plt.show()
```  
Output:  
![Figure_1](https://user-images.githubusercontent.com/22015224/199124529-a86606ee-da2a-43ce-9880-e8e27dd43cf5.png)  
![Figure_2](https://user-images.githubusercontent.com/22015224/199124569-9c3a895d-0bdb-4ccf-babf-fb8a3d2e2e44.png)  
![Figure_3](https://user-images.githubusercontent.com/22015224/199124593-ba27e264-43aa-45f9-9c20-7c5c9eff3a77.png)  
**Task 4:**  
My code for the trapezoid rule is:  
```
import numpy as np

def trapezoid(f, a, b, n):
    h = (b - a) / n
    sum = .5 * (f(a) + f(b))
    for i in range(1, n):
        x = a + i * h
        fx = f(x)
        sum += fx
    sum *= h

    return sum
```
I created code to test this:  
```
import numpy as np
from trapezoid import trapezoid

for i in range(1, 5):
    n = 2 ** i
    sum = trapezoid(lambda x: np.exp(-x * x), 0, np.pi / 4, n)
    print("n = ", n, "sum = ", sum)
```  
Output:  
```
n =  2 sum =  0.6388862805734845
n =  4 sum =  0.6471507696813964
n =  8 sum =  0.6491991053630145
n =  16 sum =  0.6497100964398593
```  
**Task 5:**  
My code for Simpson's rule is:  
```
import numpy as np

def simpson(f, a, b, n):
    h = (b - a) / n
    sum = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        fx = f(x)
        if i % 2 == 0:
            sum += 2 * fx
        else:
            sum += 4 * fx
    sum *= h / 3

    return sum
```  
My code to test this is:  
```
import numpy as np
from simpson import simpson

for i in range(1, 5):
    n = 2 ** i
    sum = simpson(lambda x: np.exp(-x * x), 0, np.pi / 4, n)
    print("n = ", n, "sum = ", sum)
```  
Output:  
```
n =  2 sum =  0.6503097748895396
n =  4 sum =  0.6499055993840337
n =  8 sum =  0.6498818839235537
n =  16 sum =  0.6498804267988076
```  
My code to find the estimation of accuracy is:  
```
import numpy as np
from simpson import simpson
import matplotlib.pyplot as plt

def compconvergence(n):
    logError = []
    logH = []
    f = lambda x: np.exp(-x * x)
    exact = simpson(f, 0, np.pi / 4, 1000)
    for i in range(0, 8):
        sum = simpson(f, 0, np.pi / 4, n)
        error = abs(exact - sum)
        logError.append(np.log(error))
        logH.append(np.log(1 / n))
        n *= 2
    return logH, logError

logH, logError = compconvergence(4)
plt.plot(logH, logError)
plt.xlabel("log(h)")
plt.ylabel("log(error)")
plt.title("Convergence of Simpson's Rule")
plt.show()
```  
Output:  
![Figure_1](https://user-images.githubusercontent.com/22015224/199138125-7a4cde09-c594-496a-9abf-e74f4ca2e8da.png)

**Root finding methods**
```
import numpy as np

def g1(x, function):
    gval = x - f_of_x(x)
    return gval

def g2(x, function):
    gval = x + f_of_x(x)
    return gval

def functionalIteration(g, x0, tol, maxIter):
    # g must be a function taking a SINGLE numeric parameter
    function = g
    y0 = x0
    tol = .0000001
    error = 10.0 * tol
    maxiter = 25
    iteration = 0

    while (error > tol and iteration < maxiter):
        x1 = g1(x0, function)
        error = np.abs(x1 - x0)
        print(f"iter: {iteration}, x0={x0}, g1(x0)={x1}")
        x0 = x1
        iteration = iteration + 1

    print("g1 approximation: ", x1)
    error = 10.0 * tol
    iteration = 0

    while (error > tol and iteration < maxiter):
        y1 = g2(y0, function)
        error = np.abs(y1 - y0)
        print(f"iter: {iteration}, x0={y0}, g2(x0)={y1}")
        y0 = y1
        iteration = iteration + 1
    print("g2 approximation: ", y1)


def f_of_x(x):
    return x * np.exp(-x)


functionalIteration(f_of_x, 3, .0000001, 25)


import numpy as np

def functionalIteration(g, x0, tol, maxIter):
    # g must be a function taking a SINGLE numeric parameter
    function = g
    y0 = x0
    tol = .0000001
    error = 10.0 * tol
    maxiter = 25
    iteration = 0

    while (error > tol and iteration < maxiter):
        x1 = g(x0)
        error = np.abs(x1 - x0)
        print(f"iter: {iteration}, x0={x0}, fx(x0)={x1}")
        x0 = x1
        iteration = iteration + 1

    print("fx approximation: ", x1)
    error = 10.0 * tol
    iteration = 0

def f_of_x(x):
    return x - 10.14 * np.exp(x * x) * np.cos(np.pi / x)

functionalIteration(f_of_x, 2, .0000001, 25)

import numpy as np

def f_of_x(x):
    return x - x * np.exp(-x)

def h_of_x(x):
    return x + x * np.exp(-x)

def l_of_x(x):
    return x - 10.14 * np.exp(x * x) * np.cos(np.pi / x)

c = 0

def bisection(g, a, b, tol):
    fa = eval(f_of_x(a))
    fb = eval(f_of_x(b))
    k = (np.log(tol) - np.log(tol)) / np.log(.5)

    for i in range (0, k):
        c = .5 * (a + b)
        fc = eval(f_of_x(c))
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    return c

def bisection2(g, a, b, tol):
    ha = eval(h_of_x(a))
    hb = eval(h_of_x(b))
    k = (np.log(tol) - np.log(tol)) / np.log(.5)

    for i in range (0, k):
        c = .5 * (a + b)
        hc = eval(h_of_x(c))
        if ha * hc < 0:
            b = c
            hb = hc
        else:
            a = c
            ha = hc

    return c

def bisection3(g, a, b, tol):
    la = eval(l_of_x(a))
    lb = eval(l_of_x(b))
    k = (np.log(tol) - np.log(tol)) / np.log(.5)

    for i in range (0, k):
        c = .5 * (a + b)
        lc = eval(l_of_x(c))
        if la * lc < 0:
            b = c
            lb = lc
        else:
            a = c
            la = lc

    return c

bisection(f_of_x(x), -1, 1, .0000001)
print("f(x) approximation is: ", c)
bisection2(h_of_x(x), -1, 1, .0000001)
print("h(x) approximation is: ", c)
bisection3(l_of_x(x), 1, 3, .0000001)
print("l(x) approximation is: ", c)
```

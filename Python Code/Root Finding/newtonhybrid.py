import numpy as np


def f_of_x(x):
    return 10.14 * np.exp(x * x) * np.cos(np.pi / x)


def d_of_x(x):
    return 10.14 * (2 * x * np.exp(x * x) * np.cos(np.pi / x) + (np.pi * np.exp(x * x) * np.sin(np.pi / x) /(x * x)))


def newtonHybrid(func, a, b, tol, maxIter):
    error = 10 * tol
    iteration = 0
    x0 = .5 * (a + b)
    while (error > tol and iteration < maxIter):
        x1 = x0 - (f_of_x(x0) / d_of_x(x0))
        newtError = np.abs(x1 - x0)
        if newtError > error:
            for i in range(1, 4):
                c = .5 * (a + b)
                fa = f_of_x(a)
                fb = f_of_x(b)
                fc = f_of_x(c)
                if fa * fc < 0:
                    b = c
                    fb = c
                elif fb * fc < 0:
                    a = c
                    fa = fc
            error = np.abs(b - a)
            x0 = .5 * (a + b)
        else:
            x0 = x1
            error = newtError
            iteration += 1
        print(f"iter: {iteration}, approximation: {x0}")
    print(f"The root is found at {x0} after {iteration} iterations")

newtonHybrid(f_of_x, -3, 7, .0000001, 25)
import numpy as np

def f_of_x(x):
    return x - x * np.exp(-x)

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

bisection(f_of_x, -3, 3, .0000001)

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

newtonsMethod(f_of_x, d_of_x, 6, 10)
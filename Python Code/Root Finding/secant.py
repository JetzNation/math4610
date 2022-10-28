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

secantMethod(f_of_x, 3, 5, 5)
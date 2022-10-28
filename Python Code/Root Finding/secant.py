import numpy as np


def f_of_x(x):
    return x * np.exp(-x)

def secantMethod(func, x0, x1, maxIter):
    iteration = 0
    tol = .00000001
    error = 10 * tol

    while (iteration < maxIter and error > tol):
        fx0 = f_of_x(x0)
        fx1 = f_of_x(x1)
        xi = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)
        error = np.abs(xi - x1)
        x0 = x1
        x1 = xi
        fx0 = fx1
        iteration += 1
    print(f"The root is found at {x1} after {iteration} iterations")

secantMethod(f_of_x, -1, 1, 25)

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

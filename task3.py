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
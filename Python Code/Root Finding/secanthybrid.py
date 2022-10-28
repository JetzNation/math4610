import numpy as np

def f_of_x(x):
    return 10.14 * np.exp(x * x) * np.cos(np.pi / x)

def secantHybrid(func, a, b, tol, maxIter):
    x0 = a
    x1 = b
    error = 10 * tol
    iteration = 0

    f0 = f_of_x(x0)
    f1 = f_of_x(x1)

    while (error > tol and iteration < maxIter):
        xi = x1 - ((f1 * (x1 - x0)) / (f1 - f0))
        secantError = np.abs(xi - x1)

        if (secantError > error):
            fa = f_of_x(a)
            fb = f_of_x(b)

            for i in range(1, 4):
                c = .5 * (a + b)
                fc = f_of_x(c)

                if (fa * fc < 0):
                    b = c
                    fb = fc

                elif (fb * fc < 0):
                    a = c
                    fa = fc
            error = np.abs(b - a)

            x0 = a
            x1 = b

        else:
            x0 = x1
            x1 = xi
            f0 = f1
            f1 = f_of_x(xi)
            error = secantError
            iteration += 1
    print(f"The root is found at {x0} after {iteration} iterations")

secantHybrid(f_of_x, -3, 7, .0000001, 25)
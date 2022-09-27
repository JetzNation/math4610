**Routine Name:** Secant hybrid method  
**Author:** Andy Skabelund  
**Language:** Python  
**Description:** Same use as Secant method but it's faster.  
**Inputs:** The inputs for this program are the function that you want to find the roots of func, your left interval a, your right interval b, your tolerance tol and the maximum number of iterations maxIter.  
**Output:** This method returns the current iteration, the approximated root.  
**Usage/Example:** Example output from this program:
```
The root is found at -2.9999999999999982 after 2 iterations
```  
**Implementation/Code:** The following is the code for secantHybrid()
```
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
```  
   
**Last Modified:** September/2022

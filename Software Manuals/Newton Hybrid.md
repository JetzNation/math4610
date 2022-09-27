**Routine Name:** Newton hybrid method  
**Author:** Andy Skabelund  
**Language:** Python  
**Description:** Same use as Newton’s method but it's faster.  
**Inputs:** The inputs for this program are the function that you want to find the roots of func, your left interval a, your right interval b, your tolerance tol and the maximum number of iterations maxIter.  
**Output:** This method returns the current iteration, x0, x1, and the approximated root.  
**Usage/Example:** Example output from this program:
```
iter: 1, approximation: 2.0
The root is found at 2.0 after 1 iterations
```  
**Implementation/Code:** The following is the code for secantMethod()
```
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
```  
   
**Last Modified:** September/2022

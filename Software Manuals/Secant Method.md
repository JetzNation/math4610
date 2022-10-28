**Routine Name:** Secant method  
**Author:** Andy Skabelund  
**Language:** Python  
**Description:** In numerical analysis, the secant method is a root-finding algorithm that uses a succession of roots of secant lines to better approximate a root of a function f.  
**Inputs:** The inputs for this program are the function that you want to find the roots of func, your first initial guess x0, your second initial guess x1, and the maximum number of iterations maxIter.  
**Output:** This method returns the current iteration, x0, x1, and the approximated root.  
**Usage/Example:** Example output from this program:
```
iter: 5, x0=5.224472906197865, x1=-0.49420805494470565, approximation: -0.49420805494470565
The root is found at -0.49420805494470565 after 5 iterations
```  
**Implementation/Code:** The following is the code for secantMethod()
```def secantMethod(func, x0, x1, maxIter):
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
```  
   
**Last Modified:** September/2022

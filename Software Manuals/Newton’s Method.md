**Routine Name:** Newton’s method
**Author:** Andy Skabelund
**Language:** Python
**Description:** Newton's method is a technique for solving equations of the form f(x)=0 by successive approximation. The idea is to pick an initial guess x0 such that f(x0) is reasonably close to 0. We then find the equation of the line tangent to y=f(x) at x=x0 and follow it back to the x axis at a new (and improved!) guess x1.
**Inputs:** The inputs for this program are the function that you want to find the roots of func, the derivative of that function fderiv, your initial guess x, and the maximum number of iterations maxIter.
**Output:** This method returns the current iteration, and the approximated root.
**Usage/Example:** Example output from this program:
```iter: 9, approximation: 17.11234335901345
The root is found at 17.11234335901345 after 10 iterations```
**Implementation/Code:** The following is the code for newtonsMethod()
```def newtonsMethod(func, fderiv, x, maxIter):
    iteration = 0

    while (iteration < maxIter):
        i = x - (f_of_x(x) / d_of_x(x))
        x = i
        print(f"iter: {iteration}, approximation: {x}")
        iteration += 1
    print(f"The root is found at {x} after {maxIter} iterations")```
    **Last Modified:** September/2022

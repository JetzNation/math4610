**Task 1**  
The code from this assignment can be found at this address  
https://github.com/JetzNation/math4610/tree/main/C%20code  

**Task 2**  
Below is my newton’s method code:  
```
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double newtonsMethod();
double fval(double);
double fpval(double);

double newtonsMethod(double (*f)(), double (*fp)(), double x0, double tol, double maxIter)
{
    double error = 10.0 * tol;
    double iteration = 0.0;
    while(error > tol && iteration < maxIter)
    {
        double f0 = f(x0);
        double fp0 = fp(x0);
        double x1 = (x0 - f0) / fp0;
        error = fabs(x1 - x0);
        x0 = x1;
        iteration = iteration + 1.0;
    }
    return x0;
}
```  
My output from the newton’s method code is:  
```
newton's method root: 0.000000
```  
**Task 3**  
The test file produces the following output:  
```
bisection root: 0.000000

 functional iteration root: 0.000000

 newton's method root: 0.000000

 secant method root: 0.000000

 newton hybrid root: 0.000000

 secant hybrid root: 0.000000
 ```  
 **Task 4**  
Below is the result of my shared library creation:  
<img width="770" alt="task 4" src="https://user-images.githubusercontent.com/22015224/194453219-0147a5d6-33c8-4f7d-946d-e0d7d050ab1d.png">  
**Task 5**  
Below is the result of my shared library test file. The output is the same as before:  
<img width="750" alt="task 5" src="https://user-images.githubusercontent.com/22015224/194453773-c164a75e-73e2-4f17-97a5-2032a3b84c54.png">

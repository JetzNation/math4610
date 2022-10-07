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
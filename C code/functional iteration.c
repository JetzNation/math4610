#include <stdio.h>
#include <stdlib.h>
#include <math.h>


double functionalIteration();
double fval(double);

double functionalIteration(double (*f)(), double x0, double tol, double maxIter)
{
    double error = 10.0 * tol;
    double iteration = 0.0;
    while(iteration < maxIter && error > tol)
    {
        double x1 = x0 - f(x0);
        error = fabs(x1 - x0);
        x0 = x1;
        iteration = iteration + 1.0;
    }
    return x0;
}
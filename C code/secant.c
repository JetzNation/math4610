#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double secantMethod();

double secantMethod(double (*f)(), double x0, double x1, double tol, double maxIter)
{
    double error = 10.0 * tol;
    double iteration = 0.0;
    double f0 = f(x0);
    double f1 = f(x1);
    while(error > tol && iteration < maxIter)
    {
        double xi = x1 - (f1 * (x1 - x0)) / (f1 - f0);
        error = fabs(xi - x1);
        x0 = x1;
        x1 = xi;
        f0 = f1;
        f1 = f(xi);
        iteration = iteration + 1.0;
    }
    return x1;
}
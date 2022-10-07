#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double bisect();
double functionalIteration();
double newtonHybrid();
double newtonsMethod();
double secantHybrid();
double secantMethod();
double fval(double);
double fpval(double);

int main()
{
    double a = -0.4;
    double b = 0.9;
    double tol = 0.0000001;
    double maxIter = 25.0;

    double rval1 = bisect(fval, a, b, tol);
    double rval2 = functionalIteration(fval, a, tol, maxIter);
    double rval3 = newtonsMethod(fval, fpval, a, tol, maxIter);
    double rval4 = secantMethod(fval, a, b, tol, maxIter);
    double rval5 = newtonHybrid(fval, fpval, a, b, tol, maxIter);
    double rval6 = secantHybrid(fval, a, b, tol, maxIter);

    printf("\n bisection root: %f\n", rval1);
    printf("\n functional iteration root: %f\n", rval2);
    printf("\n newton's method root: %f\n", rval3);
    printf("\n secant method root: %f\n", rval4);
    printf("\n newton hybrid root: %f\n", rval5);
    printf("\n secant hybrid root: %f\n", rval6);
}
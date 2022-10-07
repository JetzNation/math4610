#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double fval(double);

double fval (double xval)
{
    double fval = xval * exp(-xval);
    return fval;
}
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double fpval(double);

double fpval(double xval)
{
    double fpval = exp(-xval) - xval * exp(-xval);
    return fpval;
}
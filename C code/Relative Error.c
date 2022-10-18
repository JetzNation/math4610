#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double relativeError();

double relativeError(double approx, double exact) 
{
    double rError = fabs(approx - exact) / exact;
    return rError;
}
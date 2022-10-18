#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double absoluteError(double approx, double exact) {
    double aError = fabs(approx - exact);
    return aError;
}
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double bisect();
double fval(double);

double bisect(double (*f)(), double a, double b, double tol)
{
    double fa = f(a);
    double fb = f(b);

    if(fa * fb >= 0.0)
    {
        printf("There may not be a root in [a, b]: f(a)*f(b) = %e", fa*fb);
        exit(-1);
    }
    double c;
    double fc;

    int k = ((int) (log(tol) - log(b-a)) / log(0.5) + 1);

    for(int i=0; i<k; i++)
    {
        c = 0.5 * ( a + b);
        fc = f(c);

        if(fa*fc < 0.0)
        {
            b = c;
            fb = fc;
        } else {
            a = c;
            fa = fc;
        }
        }
        return c;
    }
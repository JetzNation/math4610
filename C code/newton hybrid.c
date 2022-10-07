#include <stdio.h>
#include <stdlib.h>
#include <math.h>


double newtonHybrid();
double fval(double);
double fpval(double);


double newtonHybrid(double (*f)(), double (*fp)(), double a, double b, double tol, double maxIter)
{
    double x0 = 0.5 * (a + b);
    double error = 10.0 * tol;
    double iteration = 0.0;
    while(error > tol && iteration < maxIter)
    {
        double f0 = f(x0);
        double fp0 = fp(x0);
        double x1 = (x0 - f0) / fp0;
        double newtError = fabs(x1 - x0);
        if(newtError > error)
        {
            double fa = f(a);
            double fb = f(b);
            double c;
            double fc;
            int k = 4.0;
            for(int i = 0; i < k; i++)
            {
                c = 0.5 * (a + b);
                fc = f(c);
                if(fa * fc < 0.0)
                {
                    b = c;
                    fb = fc;
                } else {
                    a = c;
                    fa = fc;
                }
            }
            error = fabs(b - a);
            x0 = 0.5 * (a + b);
        } else {
            x0 = x1;
            error = newtError;
            iteration = iteration + 1.0;
        }
    }
    return x0;
}

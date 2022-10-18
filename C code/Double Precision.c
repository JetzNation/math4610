#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float singlePrecision();

float singlePrecision()
{
    double one = 1.0;
    double deps = 1.0;
    double appone = 1.0;
    double count = 0.0;

    for(int i = 0; i < 101; i++)
    {
        appone = appone + deps;
        if(fabs(appone - one) == 0.0)
        {
            count++;
            printf("loops: %f\n", count);
            printf("double precision machine epsilon = %f", deps);
            break;
        } else {
            deps = deps * .5;
            count++;
        }
    }
}
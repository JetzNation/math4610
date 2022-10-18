#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float singlePrecision();

float singlePrecision()
{
    float one = 1.0f;
    float seps = 1.0f;
    float appone = 1.0f;
    double count = 0.0;

    for(int i = 0; i < 101; i++)
    {
        appone = appone + seps;
        if(fabs(appone - one) == 0.0f)
        {
            count++;
            printf("loops: %f\n", count);
            printf("single precision machine epsilon = %f", seps);
            break;
        } else {
            seps = seps * .5f;
            count++;
        }
    }
}
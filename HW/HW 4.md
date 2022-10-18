**Name:** Andy Skabelund  
**Task 1:**  
<img width="403" alt="Screen Shot 2022-10-17 at 4 59 39 PM" src="https://user-images.githubusercontent.com/22015224/196300200-7ec86b4f-2fe7-4f3b-8cf3-59baa09783ec.png">  
The expansion of this Taylor series goes as follows:  
<img width="632" alt="Screen Shot 2022-10-17 at 5 00 38 PM" src="https://user-images.githubusercontent.com/22015224/196300424-f985561b-760a-4873-988c-84187613a026.png">  
<img width="1107" alt="Screen Shot 2022-10-17 at 5 01 28 PM" src="https://user-images.githubusercontent.com/22015224/196300481-15840469-b6b4-4778-9cc0-76e2c9275fec.png">  
Proved.  
**Task 2:**  
The code for task 2 is:  
```
import numpy as np

def secondDerivative(f, x0, h, exact):
    f0 = f(x0)
    diff = []
    fV = []
    hV = []
    for i in range(1, 20):
        hV.append(h)
        f1 = f(x0 + h)
        f2 = f(x0 - h)
        fval = (f1 - 2 * f0 + f2) / (h * h)
        fV.append(fval)
        diff.append(fval - exact)
        h = h / 2
    return hV, fV, diff

def test():
    exact = 16 * (-np.pi ** 3 + 3 * np.pi ** 2 - 1040 * np.pi + 1040) / (np.pi ** 2 + 1040) ** 2
    hVals, fVals, diff = secondDerivative(lambda x: (x - np.pi / 2) * np.tan(x) * np.tan(x) / (x * x + 65), np.pi / 4, 1, exact)

    print("h values:\t approx:\t exact:\t difference:\t")

    for i in range(0, 19):
        print(hVals[i], "\t", fVals[i], "\t", exact, "\t", diff[i])

test()
```  
I wrote a different file that utilizes this algorithm, it is:  
```
import numpy as np
from SecondDerivative import secondDerivative
from DataFitting import dataFitting

def main():
    exact = 16 * (-np.pi ** 3 + 3 * np.pi ** 2 - 1040 * np.pi + 1040) / (np.pi ** 2 + 1040) ** 2
    hVals, fVals, diff = secondDerivative(lambda x: (x - np.pi / 2) * np.tan(x) * np.tan(x) / (x * x + 65), np.pi / 4, 1, exact)
    print("h values:\t approx:\t exact:\t difference:\t")
    for i in range(0, 19):
        print(hVals[i], "\t", fVals[i], "\t", exact, "\t", diff[i])

main()
```  
Output:  
```
h values:	 approx:	 exact:	 difference:	
1 	 0.08888433309385912 	 -0.03235131011796782 	 0.12123564321182695
0.5 	 -0.10999942340177273 	 -0.03235131011796782 	 -0.07764811328380491
0.25 	 -0.07472439472298283 	 -0.03235131011796782 	 -0.04237308460501501
0.125 	 -0.06930444457864582 	 -0.03235131011796782 	 -0.036953134460678
0.0625 	 -0.06807675204221608 	 -0.03235131011796782 	 -0.035725441924248265
0.03125 	 -0.06777699237687962 	 -0.03235131011796782 	 -0.0354256822589118
0.015625 	 -0.06770248904469156 	 -0.03235131011796782 	 -0.03535117892672374
0.0078125 	 -0.0676838903286523 	 -0.03235131011796782 	 -0.03533258021068448
0.00390625 	 -0.06767924234202383 	 -0.03235131011796782 	 -0.03532793222405601
0.001953125 	 -0.06767808045242418 	 -0.03235131011796782 	 -0.035326770334456366
0.0009765625 	 -0.06767778999164875 	 -0.03235131011796782 	 -0.035326479873680934
0.00048828125 	 -0.0676777173721348 	 -0.03235131011796782 	 -0.035326407254166976
0.000244140625 	 -0.06767769929138012 	 -0.03235131011796782 	 -0.035326389173412305
0.0001220703125 	 -0.06767769495490938 	 -0.03235131011796782 	 -0.03532638483694157
6.103515625e-05 	 -0.06767769437283278 	 -0.03235131011796782 	 -0.03532638425486496
3.0517578125e-05 	 -0.0676776971668005 	 -0.03235131011796782 	 -0.03532638704883268
1.52587890625e-05 	 -0.06767771393060684 	 -0.03235131011796782 	 -0.035326403812639025
7.62939453125e-06 	 -0.06767776608467102 	 -0.03235131011796782 	 -0.0353264559667032
3.814697265625e-06 	 -0.06767797470092773 	 -0.03235131011796782 	 -0.03532666458295992
```  
**Task 3:**  
The code for task 3:  
```
import numpy as np

def dataFitting(x, y, n):
    a11 = n + 1
    a12 = x[0]
    for i in range(1, n):
        a12 = a12 + x[i]
    a21 = a12
    a22 = x[0] * x[0]
    for i in range(1, n):
        a22 = a22 + x[i] * x[i]
    b1 = y[0]
    for i in range(1, n):
        b1 = b1 + y[i]
    b2 = x[0] * y[0]
    for i in range(1, n):
        b2 = b2 + x[i] * y[i]
    detA = a11 * a22 - a12 * a21
    b = (b1 * a22 - b2 * a12) / detA
    a = (b2 * a11 - b1 * a21) / detA
    return a, b
```  
I wrote a different file that utilizes this algorithm, it is:  
```
import numpy as np
from SecondDerivative import secondDerivative
from DataFitting import dataFitting

def main():
    exact = -.0548915699521
    hVals, fVals, diff = secondDerivative(lambda x: (x - np.pi / 2) * np.tan(x) / (x * x + 65), 1, 1, exact)

    a, b = dataFitting(hVals, diff, 19)
    print("y = ", a, "\tx = ", b)

main()
```  
**Task 4:**  
Absolute error:  
```
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double absoluteError(double approx, double exact) {
    double aError = fabs(approx - exact);
    return aError;
}
```  
Relative error:  
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double absoluteError(double approx, double exact) {
    double aError = fabs(approx - exact);
    return aError;
}
```  
Single precision:  
```
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
```  
Double precision:  
```
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
```  
**Task 5:**  
Here’s the steps I took to create a shared library:  
<img width="566" alt="Screen Shot 2022-10-17 at 4 13 22 PM" src="https://user-images.githubusercontent.com/22015224/196310626-f46014e8-e2d8-4a77-b0e6-fdaba28707de.png">

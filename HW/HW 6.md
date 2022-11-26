**Name:** Andy Skabelund  
**Task 1:**  
We can use the geometry of a circle in order to accomplish this task. The function for a semi-circle is <img width="73" alt="Screen Shot 2022-11-14 at 2 49 25 PM" src="https://user-images.githubusercontent.com/22015224/201775507-e600da74-9c18-425a-8b74-072ed52b58b6.png">  
then the area is pi/2, so we can write this integral as our approximation.  
<img width="224" alt="Screen Shot 2022-11-14 at 2 54 24 PM" src="https://user-images.githubusercontent.com/22015224/201776169-c4407f7b-76a5-4a6e-8c4b-42c8022f25c5.png">  
**Task 2:**  
My code for task 2 is the following  
```
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>
#include <time.h>

void main() {
    double start, end, runtime;
    start = omp_get_wtime();
    double a, b, n, pi, h, sum, x;
    int i;
    a = -1.0;
    b = 1.0;
    n = 100000.0;
    h = (b - a) / n;
    sum = 2.0 * (sqrt(1.0 - a * a) + 2.0 * sqrt(1.0 - (b * b)));
    for (i = 1; i < n; i++) {
        x = a + i * h;
        if (i % 2 == 0) {
            sum += 4.0 * sqrt(1.0 - x * x);
        } else {
            sum += 8.0 * sqrt(1.0 - x * x);
        }
    }
    pi = sum * h / 3.0;
    end = omp_get_wtime();
    runtime = end - start;
    printf("\npi = %.20f", pi);
    printf("\nRuntime = %.10f", runtime);
}
```  
Output:  
<img width="1440" alt="Screen Shot 2022-11-25 at 8 24 39 PM" src="https://user-images.githubusercontent.com/22015224/204070717-358f534b-d172-46eb-9771-4c2ab93bc600.png">  
**Task 3**  
My code for task 3 is the following:  
```
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>
#define NUM_THREADS 8

static long num_steps = 100000;

void main()
{
    double start, end, runtime;
    start = omp_get_wtime();
    int i, nthreads;
    double pi, sum[NUM_THREADS];
    double step = 2.0 / (double)num_steps;
    omp_set_num_threads(NUM_THREADS);
    #pragma omp parallel
    {
        int i, id, nthrds;
        double x;
        id = omp_get_thread_num();
        nthrds = omp_get_num_threads();
        if (id == 0) nthreads = nthrds;
        for (i = id, sum[id] = 0.0; i < num_steps; i = i + nthrds) {
            x = -1.0 + (i + 0.5) * step;
            sum[id] += 2.0 * sqrt(1.0 - x * x);
        }
    }
    for (i = 0, pi = 0.0; i < nthreads; i++) 
        pi += sum[i] * step;
    end = omp_get_wtime();
    runtime = end - start;
    printf("\npi = %.20f", pi);
    printf("\nRuntime = %.10f", runtime);
}
```  
Output:  
```
pi = 3.14159268439715555488
Runtime = 0.0012080000
```  
**Task 4**  
Our equation for approximating Euler's constant is:  
<img width="78" alt="Screen Shot 2022-11-25 at 8 46 43 PM" src="https://user-images.githubusercontent.com/22015224/204071327-e4e80d57-87a4-462a-a87b-67df747ae740.png">  
After solving the equation we get:  
<img width="390" alt="Screen Shot 2022-11-25 at 8 50 30 PM" src="https://user-images.githubusercontent.com/22015224/204071427-9f5244a8-2dec-450b-b0c1-f7c61bd7e99a.png">  
My code for this is the following:  

**Name:** Andy Skabelund  
**Task 1:**  
My code for task 1 is the following:  
```
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void kronecker(int n, int m, int k, int l, double A[n][m], double B[k][l], double C[n*k][m*l]);

void kronecker(int n, int m, int k, int l, double A[n][m], double B[k][l], double C[n*k][m*l])
{
int i, j, h, d;
for (i = 0; i < n; i++) {
  for (j = 0; j < m; j++) {
    for (d = 0; d < l; d++) {
      C[i * k + h][j * l + d] = A[i][j] + B[h][d]
    }
   }
  }
 }
}
```  
My parallel Kronecker code is the following:  
```
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>
#define NUM_THREADS 8

void kronecker(int n, int m, int k, int l, double A[n][m], double B[k][l], double C[n*k][m*l]);

void kronecker(int n, int m, int k, int l, double A[n][m], double B[k][l], double C[n*k][m*l])
{
    omp_set_num_threads(NUM_THREADS);
    #pragma omp parallel
    {
        int i, j, h, d, id, nthreads;
        id = omp_get_thread_num();
        nthreads = omp_get_num_threads();
        for (i = 0; i < n; i++)
        {
            for (j = 0; j < m; j++)
            {
                for (h = 0; h < k; h++)
                {
                    for (d = id; d < l; d += nthreads)
                    {
                        C[i*k + h][j*l + d] = A[i][j] * B[h][d];
                    }
                }
            }
        }
    }
}
```  

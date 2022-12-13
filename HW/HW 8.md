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
Output:  
<img width="1088" alt="Screen Shot 2022-12-13 at 1 08 06 PM" src="https://user-images.githubusercontent.com/22015224/207433779-f9b4af63-ebaf-4633-b4cc-8577df60b098.png">  
**Task 2:**  
My code for task 2 is the following:  
```
Skip to content
Search or jump to…
Pull requests
Issues
Codespaces
Marketplace
Explore
 
@JetzNation 
jake-daniels16
/
math4610
Public
Code
Issues
Pull requests
Actions
Projects
Security
Insights
math4610/Linear_Algebra_Code/C Code/power_method.c
@jake-daniels16
jake-daniels16 lots of hw screenshots
Latest commit ff3481c 15 days ago
 History
 1 contributor
30 lines (28 sloc)  975 Bytes

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>

double power_method(int n, double A[n][n], double x[n], double lambda, double tol, int max_iter);
void matrix_vector_mult(int n, double A[n][n], double x[n], double y[n]);
double vector_norm(int n, double x[n]);
double dot_product(int n, double x[n], double y[n]);
void vecScalar(int n, double a, double x[n], double y[n]);

double power_method(int n, double A[n][n], double x[n], double lambda, double tol, int max_iter)
{
    double error = 10.0 * tol;
    double v[n], y[n], z[n];
    int iter = 0;
    while (error > tol && iter < max_iter)
    {
        matrix_vector_mult(n, A, x, v);
        double norm = 1 / vector_norm(n, v);
        vecScalar(n, norm, v, y);
        matrix_vector_mult(n, A, y, z);
        double lambda_1 = dot_product(n, y, z);
        x[n] = y[n];
        error = fabs(lambda_1 - lambda);
        lambda = lambda_1;
        iter = iter + 1.0;
    }
    return lambda;
}

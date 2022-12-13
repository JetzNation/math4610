**Name:** Andy Skabelund  
**Task 1:**  
My code for non-parallel matrix multiplication is the following:  
```
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void matrixMult();

void matrixMult(int n, int m, int k, double A[n][m], double B[m][k], double C[n][k]) {
    for (int l = 0; l < n; l++) {
        for (int d = 0; d < k; d++) {
            C[l][d] = 0;
        }
    }
    int h, i, j, nthrds, id;
    for (i = 0; i < n; i++) {
        for (j = 0; j < k; j++) {
            for (h = 0; h < m; h++) {
                C[i][j] += A[i][h] * B[h][j];
            }
        }
    }
}
```  
The code I wrote to test this file is:  
```
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>
void matrixMult(int n, int m, int k, double A[n][m], double B[m][k], double C[n][k]);

void main()  {
    double A[3][3], B[3][3], C[3][3];
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            A[i][j] = i + 1.0;
            B[i][j] = j + 1.0;
        }
    }
    matrixMult(3, 3, 3, A, B, C);
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("%f ", C[i][j]);
        }
        printf("\n");
        }
    }
```  
Ouput:  
<img width="543" alt="Matrix Multiplication output" src="https://user-images.githubusercontent.com/22015224/205346809-55491187-8a5e-4486-a2e5-5e2b05daf4de.png">  
My parallel code is the following:  
```
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>

#define NUM_THREADS 8
void matMult_par();

void matMult_par(int n, int m, int k, double A[n][m], double B[m][k], double C[n][k])
{
    for (int l = 0; l < n; l++)
    {
        for (int d = 0; d < k; d++)
        {
            C[l][d] = 0;
        }
    }
    omp_set_num_threads(NUM_THREADS);
    #pragma omp parallel
    {
        int i, j, h, id, nthrds;
        id = omp_get_thread_num();
        nthrds = omp_get_num_threads();
        for (i = id; i < n; i += nthrds)
        {
            for (j = 0; j < k; j++)
            {
                for (h = 0; h < m; h++)
                {
                    C[i][j] += A[i][h] * B[h][j];
                }
            }
        }
    }
}
```  
My output is the same as the non-parallel code.  
**Task 2:**  
My code for task 2 is the following:  
```
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void hadamard();

void hadamard(int n, double A[n], double B[n], double C[n]) {
    for (int i = 0; i < n; i++) {
        C[i] = A[i] * B[i];
    }
}
```  
My code to test this is:  
```
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void hadamard(int n, double A[n], double B[n], double C[n]);

void main() {
    double A[3] = {1, 2, 3};
    double B[3] = {3, 2, 1};
    double C[3];
    hadamard(3, A, B, C);
    for (int i = 0; i < 3; i++) {
        printf("%f ", C[i]);
    }
}
```  
Output:  
<img width="581" alt="Screen Shot 2022-12-13 at 11 09 12 AM" src="https://user-images.githubusercontent.com/22015224/207411830-9e5b9d1e-b37c-456a-956e-12712f00b667.png">  
**Task 3:**  
My code for task 3 is the following:  
```
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>
#define NUM_THREADS 8

void hadamard_parallel();

void hadamard_parallel(int n, double A[n], double B[n], double C[n]) 
{
    omp_set_num_threads(NUM_THREADS);
    #pragma omp parallel 
    {
        int i, id, nthrds;
        id = omp_get_thread_num();
        nthrds = omp_get_num_threads();
        for (i = id; i < n; i += nthrds) 
        {
            C[i] = A[i] * B[i];
        }
    }
}
```  
My output is the same as the non-parallel version.  
**Task 4:**  
My code for task 4 is the following:  
```
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void hadamard_matrix();


void hadamard_matrix(int n, int m, double A[n][m], double B[n][m], double C[n][m]) {
    int i, j;
    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {
            C[i][j] = A[i][j] * B[i][j];
        }
    }
}
```  
My code to test this code is:  
```
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void hadamard_matrix(int n, int m, double A[n][m], double B[n][m], double C[n][m]);

void main() {
    double A[10][10], B[10][10], C[10][10];
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            A[i][j] = i;
            B[i][j] = j;
        }
    }
    hadamard_matrix(10, 10, A, B, C);

    for (int i = 0; i < 10; i++) 
    {
        for (int j = 0; j < 10; j++) 
        {
            printf("%f ", C[i][j]);
        }
        printf("\n");
    }
}
```  
Output:  
<img width="575" alt="Screen Shot 2022-12-13 at 12 12 03 PM" src="https://user-images.githubusercontent.com/22015224/207424323-84888514-329b-40fe-bd50-28cbf20acef5.png">  
**Task 5:**  
My code for task 5 is the following:  
```
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void outer_product(int n, int m, double A[n][m], double B[n][m], double C[n][m]) {
    int i, j;
    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {
            C[i][j] = A[i] * B[j];
        }
    }
}
```  
My code to test this code is the following:  
```
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void outer_product(int n, int m, double A[n][m], double B[n][m], double C[n][m]);

void main() {
    double A[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    double B[10] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
    double C[10][10];
    outer_product(10, 10, A, B, C);
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            printf("%f ", C[i][j]);
        }
        printf("\n");
    }
}
```  
Output:  
<img width="1076" alt="Screen Shot 2022-12-13 at 12 23 28 PM" src="https://user-images.githubusercontent.com/22015224/207426086-7ca574da-8aa7-4cb6-a1bc-67d8cd5e4add.png">

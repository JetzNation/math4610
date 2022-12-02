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


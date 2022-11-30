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
```
from ExplicitEuler import explicitEuler

def eApprox(f, x0, t0, T, n):
    t, x = explicitEuler(f, x0, t0, T, n)
    return x[n - 1]

n = 10

for i in range(6):
    approximation = eApprox(lambda t, x: x, 1, 0, 1, n)
    print("n :", n, "e approximation :", approximation)
    n *= 10
```  
Output:  
```
n : 10 e approximation : 2.357947691
n : 100 e approximation : 2.6780334944767583
n : 1000 e approximation : 2.7142097225133828
n : 10000 e approximation : 2.7178741394112853
n : 100000 e approximation : 2.7182410547639475
n : 1000000 e approximation : 2.718277751041721
```  
**Task 5:**  
The code I wrote for this task is the following:  
**Vector Addition:**  
```
def matrixAddition(A, B):
    C = []
    for i in range(len(A)):
        C.append([])
        for j in range(len(A[i])):
            C[i].append(A[i][j] + B[i][j])
    return C
```  
**Vector Subtraction:**. 
```
def matrixSubtraction(A, B):
    C = []
    for i in range(len(A)):
        C.append([])
        for j in range(len(A[i])):
            C[i].append(A[i][j] - B[i][j])
    return C
```
**Vector Scalar Multiplication:**  
```
def vectorScalar(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i] * b)
    return c
```  
**L1 Norm:**  
```
def L1Norm(a):
    sum = 0
    for i in range(len(a)):
        sum += abs(a[i])
    return sum
```  
**Infinity Norm:**  
```
def infNorm(a):
    max = 0
    for i in range(len(a)):
        if abs(a[i]) > max:
            max = abs(a[i])
    return max
```  
**L2 Norm:**  
```
import numpy as np

def L2Norm(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]**2
    return np.sqrt(sum)
```  
**Dot Product:**  
```
def dotProduct(a, b):
    if len(a) != len(b):
        print("Error: vectors must be of equal length")
        return None
    else:
        sum = 0
        for i in range(len(a)):
            sum += a[i] * b[i]
        return sum
```  
**Cross Product:**  
```
def crossProduct(a, b):
    if len(a) != 3 or len(b) != 3:
        print("Error: vectors must be of length 3")
        return None
    else:
        c = []
        c1 = a[1] * b[2] - a[2] * b[1]
        c2 = a[2] * b[0] - a[0] * b[2]
        c3 = a[0] * b[1] - a[1] * b[0]
        c.append(c1)
        c.append(c2)
        c.append(c3)
        return c
```  
**Triple Product:**  
```
from DotProduct import dotProduct
from CrossProduct import crossProduct

def tripleProduct(a, b, c):
    if len(a) != 3 or len(b) != 3 or len(c) != 3:
        print("Error: vectors must be of length 3")

    else:
        return dotProduct(a, crossProduct(b, c))
```  
My test code is the following:  
```
from CrossProduct import crossProduct
from DotProduct import dotProduct
from L1Norm import L1Norm
from L2Norm import L2Norm
from LInf   import infNorm
from TripleProduct import tripleProduct
from VectorAddition import vectorAddition
from VectorScalar import vectorScalar
from VectorSubtraction import vectorSubtraction

def main():
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [7, 8, 9]
    v1 = vectorAddition(a, b)
    v2 = vectorSubtraction(a, b)
    v3 = vectorScalar(a, 2)
    v4 = crossProduct(a, b)
    v5 = tripleProduct(a, b, c)
    v6 = L1Norm(a)
    v7 = L2Norm(a)
    v8 = infNorm(a)
    v9 = dotProduct(a, b)
    print("v1 = ", v1)
    print("v2 = ", v2)
    print("v3 = ", v3)
    print("v4 = ", v4)
    print("v5 = ", v5)
    print("v6 = ", v6)
    print("v7 = ", v7)
    print("v8 = ", v8)
    print("v9 = ", v9)
main()
```  
Output:  
```
v1 =  [5, 7, 9]
v2 =  [-3, -3, -3]
v3 =  [2, 4, 6]
v4 =  [-3, 6, -3]
v5 =  0
v6 =  6
v7 =  3.7416573867739413
v8 =  3
v9 =  32
```  
**Matrix Addition:**  
```
def matrixAddition(A, B):
    C = []
    for i in range(len(A)):
        C.append([])
        for j in range(len(A[i])):
            C[i].append(A[i][j] + B[i][j])
    return C
```  
**Matrix Subtraction:**  
```
def matrixSubtraction(A, B):
    C = []
    for i in range(len(A)):
        C.append([])
        for j in range(len(A[i])):
            C[i].append(A[i][j] - B[i][j])
    return C
```  
**Matrix vector product:**  
```
def matrixVectorProduct(A, b):
    if len(A[0]) != len(b):
        print("Error: incompatible dimensions")
        return None
    else:
        M = len(A)
        N = len(A[0])
        sum = 0
        c = []
        for i in range(M):
            for j in range(N):
                sum += A[i][j] * b[j]
            c.append(sum)
            sum = 0
        return c
```  
**Matrix Products:**  
```
def matrixMultiplication(A, B):
    if len(A[0]) != len(B):
        print("Error: incompatible dimensions")
        return None
    else:
        M = len(A)
        N = len(A[0])
        P = len(B[0])
        C = [[0 for i in range(P)] for j in range(M)]
        for m in range(M):
            for p in range(P):
                for n in range(N):
                    C[m][p] += A[m][n] * B[n][p]
        return C
```  
My test code is the following:  
```
from MatrixAddition import matrixAddition
from MatrixSubtraction import matrixSubtraction
from MatrixVectorProduct import matrixVectorProduct
from MatrixMultiplication import matrixMultiplication

def main():
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    a = [1, 2, 3]
    A1 = matrixAddition(A, B)
    A2 = matrixSubtraction(A, B)
    A3 = matrixVectorProduct(A, a)
    A4 = matrixMultiplication(A, B)
    print("A1 = ", A1)
    print("A2 = ", A2)
    print("A3 = ", A3)
    print("A4 = ", A4)
main()
```  
Output:  
```
A1 =  [[10, 10, 10], [10, 10, 10], [10, 10, 10]]
A2 =  [[-8, -6, -4], [-2, 0, 2], [4, 6, 8]]
A3 =  [14, 32, 50]
A4 =  [[30, 24, 18], [84, 69, 54], [138, 114, 90]]
```

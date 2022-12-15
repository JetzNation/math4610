**Routine Name:** Matrix Addition  
**Author:** Andy Skabelund  
**Language:** Python  
**Description:** Code to add matrices.  
**Inputs:** The inputs for this program are A, a matrix, and B, a matrix.  
**Output:** This method returns the computed matrix C.  
**Usage/Example:** Example output from this program:  
```
C =  [5, 7, 9]
```  
**Implementation/Code:** The following is code for matrixAddition()  
```
def matrixAddition(A, B):
    C = []
    for i in range(len(A)):
        C.append([])
        for j in range(len(A[i])):
            C[i].append(A[i][j] + B[i][j])
    return C
```  
**Last modified:** December/2022

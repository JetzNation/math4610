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
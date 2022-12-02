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
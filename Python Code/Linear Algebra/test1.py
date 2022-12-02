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
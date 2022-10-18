import numpy as np

def dataFitting(x, y, n):
    a11 = n + 1
    a12 = x[0]
    for i in range(1, n):
        a12 = a12 + x[i]
    a21 = a12
    a22 = x[0] * x[0]
    for i in range(1, n):
        a22 = a22 + x[i] * x[i]
    b1 = y[0]
    for i in range(1, n):
        b1 = b1 + y[i]
    b2 = x[0] * y[0]
    for i in range(1, n):
        b2 = b2 + x[i] * y[i]
    detA = a11 * a22 - a12 * a21
    b = (b1 * a22 - b2 * a12) / detA
    a = (b2 * a11 - b1 * a21) / detA
    return a, b
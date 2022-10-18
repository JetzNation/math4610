import numpy as np
from SecondDerivative import secondDerivative
from DataFitting import dataFitting

def main():
    exact = -.0548915699521
    hVals, fVals, diff = secondDerivative(lambda x: (x - np.pi / 2) * np.tan(x) / (x * x + 65), 1, 1, exact)

    a, b = dataFitting(hVals, diff, 19)
    print("y = ", a, "\tx = ", b)

main()
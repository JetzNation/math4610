import numpy as np
from SecondDerivative import secondDerivative

def main():
    exact = 16 * (-np.pi ** 3 + 3 * np.pi ** 2 - 1040 * np.pi + 1040) / (np.pi ** 2 + 1040) ** 2
    hVals, fVals, diff = secondDerivative(lambda x: (x - np.pi / 2) * np.tan(x) * np.tan(x) / (x * x + 65), np.pi / 4, 1, exact)
    print("h values:\t approx:\t exact:\t difference:\t")
    for i in range(0, 19):
        print(hVals[i], "\t", fVals[i], "\t", exact, "\t", diff[i])

main()
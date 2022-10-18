import numpy as np

def secondDerivative(f, x0, h, exact):
    f0 = f(x0)
    diff = []
    fV = []
    hV = []
    for i in range(1, 20):
        hV.append(h)
        f1 = f(x0 + h)
        f2 = f(x0 - h)
        fval = (f1 - 2 * f0 + f2) / (h * h)
        fV.append(fval)
        diff.append(fval - exact)
        h = h / 2
    return hV, fV, diff

def test():
    exact = 16 * (-np.pi ** 3 + 3 * np.pi ** 2 - 1040 * np.pi + 1040) / (np.pi ** 2 + 1040) ** 2
    hVals, fVals, diff = secondDerivative(lambda x: (x - np.pi / 2) * np.tan(x) * np.tan(x) / (x * x + 65), np.pi / 4, 1, exact)

    print("h values:\t approx:\t exact:\t difference:\t")

    for i in range(0, 19):
        print(hVals[i], "\t", fVals[i], "\t", exact, "\t", diff[i])

test()
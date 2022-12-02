import numpy as np

def L2Norm(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]**2
    return np.sqrt(sum)
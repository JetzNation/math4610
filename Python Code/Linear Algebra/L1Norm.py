def L1Norm(a):
    sum = 0
    for i in range(len(a)):
        sum += abs(a[i])
    return sum
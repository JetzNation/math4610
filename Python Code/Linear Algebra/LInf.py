def infNorm(a):
    max = 0
    for i in range(len(a)):
        if abs(a[i]) > max:
            max = abs(a[i])
    return max
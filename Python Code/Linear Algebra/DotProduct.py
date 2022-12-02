def dotProduct(a, b):
    if len(a) != len(b):
        print("Error: vectors must be of equal length")
        return None
    else:
        sum = 0
        for i in range(len(a)):
            sum += a[i] * b[i]
        return sum
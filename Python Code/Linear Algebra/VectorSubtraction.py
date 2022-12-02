def vectorSubtraction(a, b):
    if len(a) != len(b):
        print(("Error: vectors must be of the same length"))
        return None
    else:
        c = []
        for i in range(len(a)):
            c.append(a[i] - b[i])
        return c
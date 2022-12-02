from DotProduct import dotProduct
from CrossProduct import crossProduct

def tripleProduct(a, b, c):
    if len(a) != 3 or len(b) != 3 or len(c) != 3:
        print("Error: vectors must be of length 3")

    else:
        return dotProduct(a, crossProduct(b, c))
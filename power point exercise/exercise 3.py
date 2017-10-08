import math
def hypotenuse(x, y):
    try:
        return math.sqrt(x**2 + y**2)
    except TypeError:
        return None
print(hypotenuse(4, 2))
print(hypotenuse("2", "4"))
print(hypotenuse(4, "2"))

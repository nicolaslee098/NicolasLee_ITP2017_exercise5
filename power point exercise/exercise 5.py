import math
add,sub,mul,div = range(4)
def calculator (a,b,calculator='+',output_format=float):
    if calculator == add:
        r = a + b
        print(r)
    elif calculator == sub:
        r = a - b
        print(r)
    elif calculator == mul:
        r = a * b
        print(r)
    elif calculator == div:
        r = a / b
        print(r)
    else:
        raise ValueError
    if output_format == int:
        r = round(r)
        print(r)
    elif output_format == float:
        r = float(r)
    else:
        raise ValueError
    return r
calculator(2,3.0)
calculator(2,3.0,add,int)
calculator(2,3.0,div)
calculator(2,3.0,div,int)

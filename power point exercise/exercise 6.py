import math
add,sub,mul,div = range(4)
def calculator (a,b,opr='+',output_format=float):
    if opr == add:
        r = a + b
        print(r)
    elif opr == sub:
        r = a - b
        print(r)
    elif opr == mul:
        r = a * b
        print(r)
    elif opr == div:
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
print(calculator(input('a'), input('b'), input('opr')))

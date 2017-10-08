def factorial_recursive(a):
    try:
        if a == 0:
            return 1
        elif a == 1:
            return 1
        else:
            return a*factorial_recursive(a-1)
    except(RecursionError,TypeError):
        return None
b = float(input('no: '))
if b > 1:
    print(int(factorial_recursive(b)))
elif 0<b<1:
    print(1)

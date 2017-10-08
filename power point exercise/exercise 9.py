def p(a):
    b = a

    while b >= 0:
        yield b
        b -= 1

for c in p(7):
    print(c)

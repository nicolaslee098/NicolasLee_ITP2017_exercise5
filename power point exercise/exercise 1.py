def func_a():
    print('a message')
def b():
    func_a()
func_a()
b()
c = func_a
c()

def log(original_function):
    def new_function(*args, **kwargs):
        with open("log.txt", "w") as logfile:
            logfile.write("Function '%s' called with positional arguments %s and keyword arguments %s.\n" % (original_function.__name__, args, kwargs))

        return original_function(*args, **kwargs)

    return new_function

@log
def add(a, b):
    return a + b

print(add(3.5, 7))
print(log(add(3.5,7)))
with open("log.txt", "r") as logfile:
    print(logfile.read())

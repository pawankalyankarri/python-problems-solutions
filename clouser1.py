def outer():
    x = 10
    def inner():
        return x
    return inner()

gv = outer()
print(gv())
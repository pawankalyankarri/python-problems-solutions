
def dec(f):
    def innerfun():
        return f().split()
    return innerfun


def decfun(fun):
    def inner():
        res = fun()
        return res.upper()
    
    return inner
    


@decfun
@dec
def display():
    return 'we are good students'

res = display()
print(res)
s = 'we are good students'

def split(f):
    def innerfun(s):
        res = f(s)
        return res.split()
    return innerfun

def upper(fun):
    def inner(s):
        res = fun(s)
        return res.upper()
    return inner

@split
@upper
def display(s):
    return s

res = display(s)
print(res)
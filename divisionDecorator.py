def decfun(fun):
    def inner(a,b):
        if a>b:
            return fun(a,b)
        else:
            return fun(b,a)
    return inner

@decfun
def display(x,y):
    return x//y

res = display(10,5)
print(res)
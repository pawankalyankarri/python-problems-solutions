
def decfun(fun):
    def innerfun(a,b):
        if a>b:
            return fun(a,b)
        else:
            return fun(b,a)
    return innerfun
            


@decfun
def display(x,y):
    return x//y
    
    
res = display(10,5)
print(res)

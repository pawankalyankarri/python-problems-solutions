#decorators are special functions. which are use to change the behaviour of the function without modify
# the original function
#1. decorator should take another function as input
#2. it has one inner function
#3. nested function should be replica of original function 


def decfun(fun):
    def innerfun():
        res = fun()
        return res.upper()
    return innerfun

@decfun
def display():
    return 'hello world'

res = display()  # decfun(display)
print(res)

#division decorator


def decfun(f):
    def inner(a,b):
        if a>b:
            res = f(a,b)
        else:
            res = f(b,a)
            
        return res
    return inner


@decfun
def division(x,y):
    return x//y

res = division(3,15)   #  decfun(division(3,15))
print(res)



#uppercase splitting

def splitting(f):
    def inner():
        return f().split()
    return inner

def uppercase(fun):
    def innerfun():
        return fun().upper()
    return innerfun

@splitting
@uppercase
def display():
    return 'we are good students'

res = display()  # splitting(uppercase(display)) => splitting(innerfun) => inner(innerfun)
print(res)

#parameterized decorator
# you need to wrap decorator with funtion that function will take input


def wrapperfun(discount):
    def calcBill(fun):
        def innerBill(amt):
            actamt = fun(amt)
            res = actamt - (actamt*discount)/100
            return res
        return innerBill
    return calcBill

@wrapperfun(10)
def getBill(x):
    return x

res = getBill(1000)
print(res)
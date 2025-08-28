# def display():
#     return 10

# print(display())


# def listofargs(*args):
#     return sum(args)

# print(listofargs(1,2,3,4,5,6,7,8,9,10))

# def dictargs(**args):
#     return args.items()

# print(dictargs(name='siva',age=43))

#generator

# def display(n):
#     for i in range(n):
#         if i%2 == 0:
#             yield i
            
# for i in display(5):
#     print(i)


# x = 10
# def display():
#     global x
#     x = 5
#     print(x)
    
# display()
# print(x)

# def outer():
#     x = 10
#     def inner():
#         return x

#     return inner()

# print(outer())

#decorator

# def decfun(fun):
#     def inner():
#         return fun().upper()
    
#     return inner
    
# @decfun    
# def display():
#     return 'hello world'

# print(display())


# def upper(fun):
#     def inner():
#         return fun().upper()
#     return inner


# def split(f):
#     def innerfun():
#         return f().split()
#     return innerfun
    


# @split
# @upper
# def display():
#     return 'hello world'

# print(display())

# lambda

x = [1,2,3,4,5]


#map
# res = list(map(lambda x:x*2,x))
# print(res)

#filter

# res = list(filter(lambda x:x%2 == 0,x))
# print(res)

#reduce

# from functools import reduce

# res = reduce(lambda a,b:a+b,x)
# print(res)

#sorted

# x = [(1,2),(4,2),(5,8),(3,9)]

# res = sorted(x,key=lambda x:x[1])

# print(res)

#recursive functions

# def display(n):
#     print(n,end='')
#     if n == 1:
#         return
#     display(n-1)
#     print(n,end='')
    
# display(5)

#flatting

def flat(arr):
    res = []
    for i in arr:
        if isinstance(i,int):
            res.append(i)
        else:
            res.extend(flat(i))
            
    return res

res = flat([1,[2,[3,[4,[5,[5]]]]]])
print(res)
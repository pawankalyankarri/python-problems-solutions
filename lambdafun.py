add = (lambda *args:sum(args))(1,2,3,4,5,6,7,8,9)
print(add)

multi = (lambda a,b:a*b )(1,2)
print(multi)

#map
x = [1,2,3,4,5,6,7,8,9,10]

res = list(map(lambda n:n**2,x))
print(res)

#filter

res = list(filter(lambda n:n%2 == 0,x))
print(res)

#reduce

from functools import reduce
res = reduce(lambda a,b:a+b,x)
print(res)

#sorted

res = sorted(x,reverse=True)
print(res)

lst = [(1,5),(3,1),(5,0),(7,8)]

res = sorted(lst,key = lambda x:x[1])
print(res)
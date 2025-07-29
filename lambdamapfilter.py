x = [1,2,3,4,5,6,7,8,9,10]

res = list(map(lambda a:a**2,x))

res = list(filter(lambda n:n%2 == 0,x))

from functools import reduce

res = reduce(lambda a,b:a+b,x)

x = [(6,2),(3,0),(5,9)]

res = sorted(x,key=lambda x:x[1])

print(res)
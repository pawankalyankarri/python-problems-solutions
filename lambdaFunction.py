x = [1,2,3,4,5,6,7,8]

res = list(map(lambda n:n**2,x))


res = list(filter(lambda n:n%2 == 0,x))


res = sorted(x,reverse=True)


x = [(1,3),(5,2),(9,4),(98,45)]

res = sorted(x,key=lambda a:a[1])

print(res)
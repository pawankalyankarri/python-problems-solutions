# iterator is nothing but reading the data from the iterable

x = [1,2,3,4,5,6,7,8,9,10]

it = iter(x)
a = next(it)
b = next(it)
for i in it:
    print(i)
    

#enumerate

arr = ['one','two','three','four','five','six']

for ele,idx in enumerate(arr,start = 10):
    print(ele,idx)



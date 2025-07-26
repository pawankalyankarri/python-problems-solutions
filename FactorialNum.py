num = int(input('Enter a number: '))

def fact(num):
    f = 1
    while num>0:
        f*=num
        num-=1
    return f

res = fact(num)
print(res)
    
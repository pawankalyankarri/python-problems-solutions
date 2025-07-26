num = int(input('Enter a number: '))
print(str(num)[::-1])
res = 0
while num>0:
    t = num%10
    num//=10
    res = res*10+t
    
print(res)
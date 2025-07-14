num = int(input('Enter a number: '))
rev = int(str(num)[::-1])
print(rev)

res = 0
while num>0:
    t = num%10
    res = res*10+t
    num//=10
    
print('reversed number is',res)
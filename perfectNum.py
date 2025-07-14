num = int(input('Enter a number: '))
s = 0
for d in range(1,(num//2)+1):
    if num%d == 0:
       s+=d
if s == num:
    print('it is a perfect number') 
else:
    print('it is not perfect number')
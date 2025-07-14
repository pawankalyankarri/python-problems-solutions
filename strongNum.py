num = int(input('Enter a number: '))
bkp = num
fact = 1
while bkp>1:
    fact*=bkp
    bkp-=1
if num == fact:
    print('it is a strongNumber') 
else:
    print('it is not strongnumber')
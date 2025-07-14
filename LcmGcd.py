n1 = int(input('Enter a number1:'))
n2 = int(input('Enter a number2'))

if n1<n2:
    small = n1
else:
    small = n2
  
for d in range(small,1,-1):
    if n1%d == 0 and n2%d == 0:
        gcd = d
        break
else:
    gcd = 1
    

lcm = (n1*n2)//gcd
print('lcm',lcm)
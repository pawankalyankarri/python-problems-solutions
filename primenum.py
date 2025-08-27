# num = int(input('enter a number: '))

# for i in range(2,(num//2)+1):
#     if num%i == 0:
#         print(num,'is not prime')
#         break
# else:
#     print(num,'prime number')


s = int(input('enter st number'))
e = int(input('enter a end number: '))

for num in range(s,e+1):
    for d in range(2,(num//2)+1):
        if num%d == 0:
            break
    else:
        print(num,end=' ')
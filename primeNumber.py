num = int(input('Enter a number:'))
for i in range(2,(num//2)+1):
    if num%i == 0:
        print(num,'is not prime')
        break
else:
    print(num,'is  prime')
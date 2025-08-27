num = int(input('enter a number: '))

a = 0
b = 1
while True:
    c = a+b
    if c == num:
        print(num,'fibonacci')
        break
    
    if c>num:
        print(num,'is not fibonacci')
        break
    a = b
    b = c
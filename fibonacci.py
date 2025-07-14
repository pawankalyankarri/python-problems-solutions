num = int(input('Enter a number'))

a = 0
b = 1
while True:
    c = a+b
    if c == num:
        print('it is fibonacci')
        break
    if c>num:
        print('it is not fibonacci')
        break
    a = b
    b = c
    
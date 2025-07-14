num = int(input('Enter a number: '))

a = 0
b = 1
cnt = 0
while num>0:
    c = a+b
    if c%2 == 0:
        cnt+=1
        if cnt == num:
            print(c)
    a = b
    b = c
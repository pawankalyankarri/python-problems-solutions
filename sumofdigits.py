num = int(input('Enter a number: '))
while True:
    s = 0
    while num>0:
        s+= num%10
        num//=10
    if s>9:
        num = s
    else:
        print(s)
        break
start = int(input('Enter a starting number:'))
end = int(input('Enter a ending number: '))

a = 0
b = 1
while True:
    c = a+b 
    if c>=start:
        if c>end:
            break
        print(c,end=' ')
    
    a = b
    b = c

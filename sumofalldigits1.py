num = int(input('enter a number: '))

# s = 0
# while num>0:
#     s+=num%10
#     num//=10
    
# print(s)


while True:
    s = 0
    while num>0:
        s+=num%10
        num//=10
    if s>9:
        num = s
        s = 0
    else:
        print(s)
        break
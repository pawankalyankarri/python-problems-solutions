num = int(input('Enter a number'))

# s = 0
# while num>0:
#     t = num%10
#     s+=t
#     num//=10
    
# print(s)




while True:
    s = 0
    while num>0:
        s+=num%10
        num//=10
        
    if s>9:
        num = s
    else:
        print(s)
        break
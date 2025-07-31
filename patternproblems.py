rows = int(input('Enter a number: '))


# middle = (rows//2)+1
# for i in range(1,rows+1):
#     if i<middle:
#         print(' '*(middle-i)+'*'*(2*i-1))
#     else:
#         print(' '*(i-middle)+'*'*(2*rows-2*i+1))



# for i in range(1,rows+1):
#     print(' '*(rows-i)+'*'*(2*i-1))


# for i in range(1,rows+1):
#     print('*'*(i))

# for i in range(1,rows+1):
#     print(' '*(i-1)+'*'*(2*rows-2*i+1))


middle = (rows//2)+1

for i in range(1,rows+1):
    if i == 1 or i == rows:
        print(' '*(middle-1)+'*')
    elif i<middle:
        print(' '*(middle-i)+'*'+' '*(2*i-3)+'*')
    else:
        print(' '*(i-middle)+'*'+' '*(2*rows-2*i-1)+'*')
        
        
    
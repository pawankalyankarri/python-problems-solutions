rows = int(input('Enter a number: '))


# for i in range(1,rows+1):
#     print(' '*(rows-1)+'*'*i)


# for i in range(1,rows+1):
#     if i == 1 or i == rows:
#         print(' '*(rows-i)+'*'*i)
#     else:
#         print(' '*(rows-i)+'*'+' '*(i-2)+'*')


# middle = (rows//2)+1
# for i in range(1,rows+1):
#     if i<middle:
#         print(' '*(middle-i)+'*'*(2*i-1))
#     else:
#         print(' '*(i-middle)+'*'*(2*rows-2*i+1))  #22 - 12+1 =>11


middle = (rows//2)+1
for i in range(1,rows+1):
    if i == 1 or i == rows:
        print(' '*(middle-1)+'*',sep='')
    elif i<middle:
        print(' '*(middle-i)+'*'+' '*(2*i-3)+'*',sep='')
    else:
        print(' '*(i-middle)+'*'+' '*(2*rows-2*i-1)+'*',sep='')
        
    
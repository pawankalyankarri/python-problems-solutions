num = int(input('Enter a number: '))

# res = True if num == sum([ int(n)**len(str(num)) for n in str(num)]) else False
# print(res)


bkp = num
dc = 0
while bkp>0:
    bkp//=10
    dc+=1
bkp = num
s = 0
while bkp>0:
    t = bkp%10
    s = s+t**dc
    bkp//=10
    
if s == num:
    print('armstrong')
    
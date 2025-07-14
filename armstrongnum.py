num = int(input('Enter a number:'))
res = 0
bkp = num
dc = len(str(bkp))
while bkp>0:
    t = bkp%10
    res+=t**dc
    bkp//=10
    
if num == res:
    print('armstrong')
else:
    print('not armstrong')
    
#short cut way
  
if num == sum([int(n)**len(str(num)) for n in str(num)]):
    print('armstrong') 
else:
    print('not armstrong')
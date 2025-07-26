num = int(input('Enter a number: '))

def strong(num):
    bkp = num
    s = 0
    while bkp>0:
        t = bkp%10
        bkp//=10
        f = 1
        while t>1:
            f*=t
            t-=1
        s+=f
    if s == num:
        return True
    else:
        return False
    
        
           
       
    
    
print(strong(num))
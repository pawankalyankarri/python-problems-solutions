x = [58,39,29,56,96,12,13,15,19,60]


num = int(input('Enter a number'))
x.sort()
s = 0
e = len(x)-1
for _ in x:
    middle = (s+e)//2
    if s>e:
        print(num,'is not found')
        break
    elif x[middle] == num:
        print(num,'is found')
        break
    elif x[middle] > num:
        e = middle-1
    elif x[middle] < num:
        s = middle+1
    else:
        pass
    
        
    


























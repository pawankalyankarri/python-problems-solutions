x = [58,39,29,56,96,12,13,15,19,60]

def binary(x,s,e,n):
    m = (s+e)//2
    if s>e:
        return False
    elif x[m] == n:
        return True
    elif x[m] > n:
        return binary(x,s,m-1,n)
    elif x[m]< n:
        return binary(x,m+1,e,n)
    else:
        pass
    
res = binary(x,0,len(x),12)
print(res)
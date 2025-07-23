d = {'y':10,'z':1,'a':100,'b':20}

x = list(d.items())

for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i][1] > x[j][1]:
            x[i],x[j] = x[j],x[i]
            
res = dict(x)
print(res)
    
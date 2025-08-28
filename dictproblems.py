d = {'x':10,'z':1,'a':100,'b':20}

x = list(d.items())

for i in range(len(x)):
    for j in range(len(x)-1):
        if x[j][1]>x[j+1][1]:
            x[j],x[j+1] = x[j+1],x[j]
            
res = dict(x)

print(res)
x = [58,39,29,56,96,12,13,15,19,60]

for i in range(len(x)):
    for j in range(len(x)-1-i):
        if x[j]>x[j+1]:
            x[j],x[j+1] = x[j+1],x[j]
            
            
print(x)
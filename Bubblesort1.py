x = [58,39,29,56,96,12,13,15,19,60]

i = 0
while i<len(x)-1:
    if x[i]>x[i+1]:
        x[i],x[i+1] = x[i+1],x[i]
        i = 0
    else:
        i+=1


print(x)


for i in range(len(x)):
    for j in range(len(x)-i-1):
        if x[j]>x[j+1]:
            x[j],x[j+1] = x[j+1],x[j]
            
            
# print(x)
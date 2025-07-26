x = [1,4,7,9,34,56,789,34,566,34,485]

for i in range(len(x)):
    for j in range(len(x)-i-1):
        if x[j]> x[j+1]:
            x[j],x[j+1] = x[j+1],x[j]
            
print(x)
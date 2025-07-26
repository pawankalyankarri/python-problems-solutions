x = [1,4,7,9,34,56,789,34,566,34,485]

for i in range(len(x)):
    min_v = min(x[i:])
    idx = x[i:].index(min_v)+i
    x[i],x[idx] = x[idx],x[i]
    
print(x)
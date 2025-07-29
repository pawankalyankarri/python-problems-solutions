x = [58,39,29,56,96,12,13,15,19,60]




for i in range(len(x)):
    min_v = min(x[i:])
    idx = x[i:].index(min_v)+i
    x[idx],x[i] = x[i],x[idx]
    
print(x)















# for i in range(len(x)):
#     min_v = min(x[i:])
#     idx = x[i:].index(min_v)+i
#     x[i],x[idx] = x[idx],x[i]
    
# print(x)
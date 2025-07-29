x = {'y':10,'z':1,'a':100,'b':20}


d = list(x.items())

for i in range(len(d)):
    for j in range(len(d)-1):
        if d[j][0]>d[j+1][0]:
            d[j],d[j+1]  = d[j+1],d[j]
            
#res = dict(d)
res = { k:v for k,v in d}
print(res)












# d = list(x.items())

# for i in range(len(d)):
#     for j in range(len(d)-1-i):
#         if d[j][1]>d[j+1][1]:
#             d[j],d[j+1] = d[j+1],d[j]
            
        
            
            
# print(dict(d))
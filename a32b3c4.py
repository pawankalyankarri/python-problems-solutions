s = 'a32b3c5'

res = ''
i = 0

while i<len(s):
    if s[i].isdigit():
        for j in range(i,len(s)):
            if s[j].isalpha():
                break
        else:
            j = len(s)
            
        num = s[i:j]
        res = res+s[i-1]*int(num)
        i = j+1
    else:
        i +=1
        
        
print(res)


#char count

x = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbccccc'
d = {}
for i in x:
    d[i] = d.get(i,0)+1
    
print(d)



















# i = 0
# res = ''
# while i<len(s):
#     if s[i].isdigit():
#         for j in range(i,len(s)):
#             if s[j].isalpha():
#                 break
#         else:
#             j = len(s)
#         num = s[i:j]
#         res = res + s[i-1]*int(num)
#         i = j+1
#     else:
#         i+=1
        
        
# print(res)
        
s = 'apple'


c_list = []

for i in range(len(s)):
    if s[i] not in c_list:
        cnt = 0
        for j in range(i,len(s)):
            if s[i] == s[j]:
                cnt+=1
        print(s[i],cnt)
        c_list.append(s[i])
        
















# c_list = []

# for i in s:
#     if i not in c_list:
#         cnt = s.count(i)
#         print(i,cnt)
#         c_list.append(i)
        
        
    














# d = {}
# for i in s:
#     d[i] = d.get(i,0)+1
    
# print(d)
s = 'aaabbcddaaaa'

res = ''

pre_ch = s[0]
cnt = 0
for ch in s:
    if ch == pre_ch:
        cnt+=1
    else:
        print(pre_ch,cnt)
        cnt = 1
        pre_ch = ch
        
else:
    print(pre_ch,cnt)
        

        
























# res = ''
# pre_ch = s[0]
# cnt = 0

# for ch in s:
#     if ch == pre_ch:
#         cnt+=1
#     else:
#         res = res+pre_ch+str(cnt)
#         pre_ch = ch
#         cnt = 1
# else:
#     res = res+pre_ch+str(cnt)
    
# print(res)




















    

s = 'aaabbcddaaaa'

res = ''
pre_ch = s[0]
cnt = 0

for ch in s:
    if ch == pre_ch:
        cnt+=1
    else:
        res = res+pre_ch+str(cnt)
        pre_ch = ch
        cnt = 1
else:
    res = res+pre_ch+str(cnt)
    
print(res)




















    

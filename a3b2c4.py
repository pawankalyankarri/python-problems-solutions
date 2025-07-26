s = 'a34b43c3d2'
res = ''
i = 0
while i<len(s):
    if s[i].isdigit():
        for j in range(i,len(s)):
            if s[j].isalpha():
                break
        else:
            j = len(s)
            
        num = int(s[i:j])
        res = res+s[i-1]*num
        i = j+1
    else:
        i+=1
        
print(res)
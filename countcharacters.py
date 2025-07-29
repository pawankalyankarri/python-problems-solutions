s = 'we are gooooooooooooooooooood'

s_word = input('enter a char')
cnt = 0
for i in range(len(s)):
    if s[i:i+len(s_word)] == s_word:
        cnt+=1
print(cnt)










# d = {}
# for ch in s:
#     d[ch] = d.get(ch,0)+1
    
# print(d)











# which = input('Enter a word: ')
# cnt  = 0
# for i in range(len(s)):
#     if s[i:i+len(which)] == which:
#         cnt += 1

# print(which,cnt)

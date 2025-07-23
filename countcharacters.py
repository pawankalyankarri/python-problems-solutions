s = 'we are gooooooooooooooooooood'

which = input('Enter a word: ')
cnt  = 0
for i in range(len(s)):
    if s[i:i+len(which)] == which:
        cnt += 1

print(which,cnt)

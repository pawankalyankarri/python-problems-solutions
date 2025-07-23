s = 'we are good students'

res = ''

for ch in s:
    a_code = ord(ch)
    if a_code>=97 and a_code<=122:
        res+=chr(a_code-32)
    else:
        res+=ch

print(res)
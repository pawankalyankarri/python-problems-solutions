s = 'we are learning python are are'

what = input('Enter a what:')
occ = int(input('Enter a occ:'))
which = input('Enter a which: ')



if what in s and  s.count(what) == occ:
    res = ''
    cnt = 0
    for i in range(len(s)):
        if s[i:i+len(what)] == what:
            cnt+=1
            if cnt == occ:
                res= s[:i]+which+s[i+len(what):]
                
    print(res)
else:
    print('not ')
    
    
    
        



















# if what in s and occ <= s.count(what):
#     res = ''
#     cnt = 0
#     for i in range(len(s)):
#         if s[i:i+len(what)] == what :
#             cnt+=1
#             if cnt == occ:
#                 res = s[:i]+which+s[i+len(what):]
                
#     print(res)












# if what in s and occ <= s.count(what):
#     res = ''
#     cnt = 0
#     for i in range(len(s)):
#         if s[i:i+len(what)] == what:
#             cnt += 1
#             if cnt == occ:
#                 res = s[:i]+which+s[i+len(what):]
        
#     print(res)
    
# else:
#     print('not possible')
            
        
    
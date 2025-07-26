x = [58,39,29,56,96,12,13,15,19,60]


# num = int(input('Enter a : '))
# x.sort()
# def binary(x,s,e,num):
#     middle = (s+e)//2
#     if s>e:
#         return False
#     elif x[middle] == num:
#         return True
#     elif x[middle] > num:
#         return binary(x,s,middle-1,num)
#     elif x[middle] < num:
#         return binary(x,middle+1,e,num)
#     else:
#         pass
    
# res = binary(x,0,len(x)-1,num)
# print(res)


















# x.sort()
# num = int(input('Enter a number: '))
# s = 0
# e = len(x)-1
# for _ in range(len(x)):
#     middle = (s+e)//2
#     if s>e:
#         print(num,'not found')
#         break
#     elif x[middle] == num:
#         print(num,'is found')
#         break
#     elif x[middle] > num:
#         e = middle-1
#     elif x[middle]< num:
#         s = middle+1
#     else:
#         pass

arr = [4,32,54,76,87,12,45,7,6,456]

s = 0
e = len(arr)-1
arr.sort()
num = int(input('Enter a number: '))

for _ in arr:
    middle = (s+e)//2
    if s>e:
        print('not found')
        break
    elif arr[middle] == num:
        print('num is found')
        break
    elif arr[middle] > num:
        e = middle-1
        
    elif arr[middle] < num:
        s = middle+1
        
    else:
        pass
    
        


















# arr.sort()
# num = int(input('enter a number: '))
# s = 0
# e = len(arr)-1

# for i in arr:
#     middle = (s+e)//2
#     if s>e:
#         print(num,'is not found')
#         break
#     elif arr[middle] == num:
#         print(num,'is found')
#         break
#     elif arr[middle] > num:
#         e = middle-1
#     elif arr[middle]<num:
#         s = middle+1
#     else:
#         pass
    

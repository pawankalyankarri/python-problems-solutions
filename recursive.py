# def display(n):
#     print(n,end='')
#     if n == 0:
#         return
#     display(n-1)
#     print(n,end='')
   
   
# display(5) 


# x = [4,32,54,76,87,12,45,7,6,456]

# num = int(input('enter a number: '))
# x.sort()
# def binary(x,s,e,num):
#     middle = (s+e)//2
#     if s>e:
#         return False
#     elif x[middle] == num:
#         return True
#     elif x[middle] < num:
#         return binary(x,middle+1,e,num)
#     elif x[middle] > num:
#         return binary(x,s,middle-1,num)
#     else:
#         pass
    
# res = binary(x,0,len(x)-1,num)
# print(res)



# def fact(num):
#     if num == 1:
#         return 1
#     return num*fact(num-1)

# res = fact(5)
# print(res)

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def flat(x,res = []):
    for i in x:
        if isinstance(i,int):
            res.append(i)
        else:
            flat(i)
            
    return res

res = flat(x)

print(res)
    

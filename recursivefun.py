# def display(n):
#     print(n,end=' ')
#     if n == 1:
#         return
#     display(n-1)
#     print(n,end=' ')
    
# display(5)



x = [1,4,7,9,34,56,789,34,566,34,485]

num = int(input('Enter a number: '))
x.sort()
def binary(x,s,e,num):
    middle = (s+e)//2
    if s>e:
        return False
    elif x[middle] == num:
        return True
    elif x[middle]>num:
        return binary(x,s,middle-1,num)
    elif x[middle]<num:
        return binary(x,middle+1,e,num)
    else:
        pass
    
    
res = binary(x,0,len(x)-1,num)
print(res)


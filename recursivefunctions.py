#1-10 nums
def display(n = 1):
    if n > 10:
        return
    print(n)
    display(n+1)
    
display()

#factorial of a number

def fact(num):
    if num == 1:
        return 1
    return num*fact(num-1)

res = fact(5)
print(res)

#prime number using recursive

def isprime(num,d = 2):
    if d>num//2:
        return True
    if num % d == 0:
        return False
    return isprime(num,d+1)

res = isprime(11)
print(res)

#flat an array

x = [[1,2],[3,4,5],[4,5,[6,7,[8,9]],[11,[12],[13]],[15]]]

def flat(x,res = None):
    if res == None:
        res = []
    for i in x:
        if type(i) == int:
            res.append(i)
        else:
            flat(i,res)
    return res

res = flat(x)
print(res)
            

#binary search using recursive function

x = [43,56,23,43,12,56,7,6,5,8,2,98,68]


# normal binary search
# x.sort()
# '''num = int(input('Enter a number:'))'''
# num = 999
# s = 0
# e = len(x)-1
# for _ in x:
#     middle = (s+e)//2
#     if s>e:
#         print(num,'is not found')
#         break
#     elif x[middle] == num:
#         print(num,'is found')
#         break
#     elif x[middle] > num:
#         e = middle-1
#     elif x[middle] < num:
#         s = middle+1
#     else:
#         pass
    
    
    
x.sort()
num = 7
def binarysearch(x,s,e,num):
    middle = (s+e)//2
    if s>e:
        return False
    elif x[middle] == num:
        return True
    elif x[middle] < num:
        return binarysearch(x,middle+1,e,num)
    elif x[middle] > num:
        return binarysearch(x,s,middle-1,num)
    else:
        pass
    
res = binarysearch(x,0,len(x)-1,num)
print(res)

#543212345

def display(num):
    print(num,end='')
    if num == 1:
        return 
    display(num-1)
    print(num,end='')
    
display(5)
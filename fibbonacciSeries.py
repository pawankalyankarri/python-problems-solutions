# n = int(input('Enter a number: '))

# a = 0
# b = 1
# cnt = 2
# print(a,b,end='')
# while True:
#     c = a+b
#     cnt+=1
#     print(c,end=' ')
#     if cnt == n:
#         break
#     a = b 
#     b = c


num = int(input('Enter a number: '))

a = 0
b = 1

while True:
    c = a+b
    if c == num:
        print(num,'is fibonacci')
        break
    if c>num:
        print(num,'is not fibboncci')
        break
    a = b
    b = c
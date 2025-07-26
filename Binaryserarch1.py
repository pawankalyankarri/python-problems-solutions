num = int(input('Enter a number'))

x = [1,4,7,9,34,56,789,34,566,34,485]
s = 0
e = len(x)-1
x.sort()

for _ in x:
   middle = (s+e)//2
   if s>e:
       print(num,'is not found')
       break
   elif x[middle] == num:
       print(num,'is found')
       break
   elif x[middle] > num:
       e = middle-1
   elif x[middle] < num:
       s = middle+1
   else:
       pass
       
arr = [33,54,63,23,134,6,45,345,456,111]

first = float('-inf')
second = float('-inf')
for num in arr:
    if num>first:
        second = first
        first = num
    if num<first and num>second:
        second = num
print('second max num is',second)

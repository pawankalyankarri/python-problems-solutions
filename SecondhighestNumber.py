x = [1,4,7,9,34,56,789,34,566,34,485]

first = float('-inf')
second = float('-inf')

for i in x:
    if i>first:
        second = first
        first = i
    if i>second and i<first:
        second = i

print(second)
start = int(input('Enter starting num:'))
end = int(input('Enter a ending num:'))
if start<2:
    start = 2
for num in range(start,end+1):
    for d in range(2,(num//2)+1):
        if num%d == 0:
            break
    else:
        print(num,end=' ')
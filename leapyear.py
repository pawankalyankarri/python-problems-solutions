year = int(input('Enter a number: '))

if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
    print('it is leap year')
    
else:
    print(year,'not leap year')
num = int(input('Enter a number: '))

decimal = [1,4,5,9,10,40,50,90,100]
roman = ['I','IV','V','IX','X','XL','L','XC','C']

decimal.reverse()
roman.reverse()

for d in decimal:
    q = num//d
    if q>0:
        idx = decimal.index(d)
        print(roman[idx]*q,end='')
        num%=d
        
        
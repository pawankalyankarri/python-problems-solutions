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

def primes(num,d = 2):
    if d > num//2:
        return True
    if num%d == 0:
        return False
    return primes(num,d+1)

res = primes(11)
print(res)
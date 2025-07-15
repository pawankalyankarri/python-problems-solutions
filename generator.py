#generator is a special function which is using yield keyword to return value by value to the calling area

def generateevens(num):
    for i in range(num+1):
        if i%2 == 0:
            yield i
            
for n in generateevens(50):
    print(n)           
    
    
    

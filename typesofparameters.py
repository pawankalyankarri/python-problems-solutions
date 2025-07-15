#1. postional arguments we should pass those
def positional(x,y):
    return x+y

res = positional(1,2)
print(res)


#2. default arguments

def default(x = 10,y = 20):
    return x+y

res = default()
print(res)

#3. keyword argumements

def keyword(name,age):
    return f'{name} and  his age is {age}'

res = keyword(age = 40,name='siva')
print(res)

#4. List of arguments

def listOfArg(*args):
    return sum(args)

res = listOfArg(1,2,3,4,5,6,7,8,9)
print(res)

#5. dictionary of keyword arguments

def dictOfKey(**kwargs):
    for k,v in kwargs.items():
        print(f'key is {k} and value is {v}')
        
dictOfKey(name='raju',age=43,gender='male')

#in any situation you need to use all these in one function 

def display(postional,listofarg,default,dicofkeyarg):
    return 'This is the order'
#if function return another function as output or if a function takes input as another function that is 
# called higher order function

def first(another):
    return another()

def display():
    return 'Hello world'

res = first(display)
print(res)
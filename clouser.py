#remembring the state of the local variable outside of the outer function is called closure

#it provides some sort of security and you can use that variable globally no one cant modify that

def outerfun():
    n = 5  #this is local variable
    def innerfun():
        return n
    return innerfun

res = outerfun()

print(res())
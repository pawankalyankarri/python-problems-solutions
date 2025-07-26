x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def flat(x,res = []):
    for i in x:
        if isinstance(i,int):
            res.append(i)
        else:
            flat(i)
            
    return res


res = flat(x)
print(res)
















# def flat(x,res= []):
#     for i in x:
#         if isinstance(i,int):
#             res.append(i)
#         else:
#             flat(i)
#     return res

# res = flat(x)
# print(res)



# num = int(input(': '))

# def fact(num):
#     if num == 1:
#         return 1
#     return fact(num-1)*num

# res = fact(num)
# print(res)
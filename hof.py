def incre(x):
    return x+1

def hof(x, func):
    return x + func(x)

increV2 = lambda x : x + 1
hofV2 = lambda x,fun : x + fun(x) 

result = hof(2, incre)
print(result)

result2 = hofV2(2, increV2)
print(result2)



from functools import reduce

numbers = [1,2,3,4]
print(numbers)

def acum (counter, item):
    return counter + item

result = reduce(acum, numbers )
print(result)

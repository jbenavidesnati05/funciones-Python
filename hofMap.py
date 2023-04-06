numbers = [1,2,3,4]
numbersV2 = []

for i in numbers:
    numbersV2.append(i*2)
    
print(numbers)
print(numbersV2)

numbersV3 = list(map(lambda i : i*2,numbers))
print(numbersV3)

numbers1 = [1,2,3,4]
print(numbers1)
numbers2 = [5,6,7]
print(numbers2)

result = list(map(lambda x,y: x + y ,numbers1,numbers2))
print(result)
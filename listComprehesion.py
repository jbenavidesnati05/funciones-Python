numbers = []

for element in range(1,11):
    numbers.append(element*2)
print(numbers)

numbers_V2 = [element*2 for element in range(1,11)]
print(numbers_V2)

numbersPares = []

for element in range(1,11):
    if element%2 == 0:
        numbersPares.append(element)
print(numbersPares)

numbersPares_V2 = [ element for element in range(1,11) if element % 2 == 0 ]
print(numbersPares_V2)
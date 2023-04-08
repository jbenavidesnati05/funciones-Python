words = ['amor', 'sol', 'piedra', 'día']
print(words)

newWords = list(filter(lambda item : len(item) >= 4 , words ))
print(newWords)
print("version larga")
diccionario  = {}

for i in range (1,5):
    diccionario[i] = i*2

print(diccionario)

print("version corta")

diccionario_V2 = {i:i*2 for i in range(1,6)}
print(diccionario_V2)
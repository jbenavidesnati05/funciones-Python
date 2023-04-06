def incrementar(x):
    return x+1
result = incrementar(10)
print(result)

incrementarLambda =  lambda x : x + 1
resultado2 = incrementarLambda(2)
print(resultado2)


nombreCompleto = lambda nombre, apellido : f"Nombre Completo: {nombre} {apellido}" 
resultado3 = nombreCompleto("andres", "paez")
print(resultado3)
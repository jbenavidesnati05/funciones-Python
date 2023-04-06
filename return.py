
def sumaConRango(min,max):
    print(f"minimo: {min}, maximo: {max}")
    sum = 0;
    for x in range(min,max):
        sum +=x
    return sum
result= sumaConRango(1,100);
print(result)

numeros = []
suma = 0
for i in range(5):
    n = int(input("ingrese un numero: "))
    numeros.append(n)
    suma += n
print(numeros)
print("la suma es: ",suma)
print("el promedio es: ",suma/len(numeros))
print("el menor numero de la lista es: ",min(numeros))
print("el mayor numero de la lista es: ",max(numeros))
numeros = []
suma = 0
n = int(input("ingrese la cantidad de elementos de la lista: "))
for i in range(n):
    num = int(input("ingrese un numero: "))
    numeros.append(num)
    suma += num
print(numeros)
print("la suma es: ",suma)
print("el promedio es: ",suma/len(numeros))
print("el menor numero de la lista es: ",min(numeros))
print("el mayor numero de la lista es: ",max(numeros))
numeros = []
suma = 0
i = 0
n = int(input("ingrese la cantidad de elementos de la lista: "))
while i < n:
    num = int(input("ingrese un numero : "))
    numeros.append(num)
    suma += num
    i += 1
print(numeros)
print("la suma es: ",suma)
print("el promedio es: ",suma/len(numeros))
print("el menor numero de la lista es: ",min(numeros))
print("el mayor numero de la lista es: ",max(numeros))
numeros = [1, 2, 3, 4, 5]

numero = int(input("Ingrese el numero: "))
posicion = int(input("Ingrese la posicion: "))
numeros.insert(posicion, numero)
print("El numero se encuentra en la posicion: ", posicion)
print (F"Lista actulizada {numeros}")

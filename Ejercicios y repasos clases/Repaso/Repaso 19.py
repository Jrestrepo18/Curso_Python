numeros = []

for i in range(5):
    numero = int(input("Ingrese los numeros: "))
    if numero % 2 == 0:
        numeros.append(numero)
    print(numeros)
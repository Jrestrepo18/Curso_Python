def ejercicio_1 ():
    nombre = input("Ingrese nombre: ")
    print(f"Hola {nombre}")

def ejercicio_2():
    num1 = int(input("Ingrese un numero: "))
    num2= int(input("Ingrese un numero: "))
    resultado = num1 + num2
    print(f" Resultado: {resultado}") 

def ejercicio_3():
    numero = int(input("Ingrese un numero: "))
    if numero % 2 == 0:
        print("Numero par")
    else:
        print("Numero impar")

def ejercicio_4():
    edad = int(input("Ingrese su edad: "))
    if edad < 18:
         print("Menor de edad.")
    else:
        print("Mayor de edad.")

def ejercicio_5():
    grados_celsius = float(input("Ingrese la temperatura en Celsius: "))
    grados_fahrenheit =(grados_celsius * 9/5) +32
    print(f"La temperatura en grados fahrenheit es: {grados_fahrenheit} ")

def ejercicio_6():
    base = float(input("Ingrese la base del triangulo: "))
    altura = float(input("Ingrese la altura del triangulo: "))

    area = (base * altura)/2

    print(f"El area del triangulo es: {area}")

def ejercicio_7():
    lista_numeros = []
    i = 0
    for i in range(5):
        numero_mayor = float(input("Ingrese los numeros a la lista: "))
        lista_numeros.append(numero_mayor)
        i = i + 1

    if lista_numeros:
        print(f"Numero mayor es: {max(lista_numeros)}")

def ejercicio_8():
    palabra = input("Ingrese una palabra: ")
    numero_letras = len(palabra)

    print(f"La palabra {palabra} tiene {numero_letras} letras.")

def ejercicio_9():
    numeros = input("Ingrese los números separados por espacio: ").split()
    pares = []

    for numero in numeros:
        if int(numero) % 2 == 0:
            pares.append(int(numero))

    print(f"Números pares son: {pares}")







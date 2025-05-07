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

def ejercicio_10():
    palabra = input("Ingrese una palabra: ")
    palabra = palabra.lower().replace(" ", "")
    if palabra == palabra[::-1]:
        print("Palabra palindromo.")
    else:
        print("La palabra no es palindromo.")

def ejercicio_12():
    entrada = input("Ingrese números separados por comas: ").split(",")
    sin_repetir = []

    for num in entrada:
        num = num.strip()
        if num.isdigit():  # verifica que sea un número
            num = int(num)
            if num not in sin_repetir:
                sin_repetir.append(num)
        else:
            print(f"'{num}' no es un número válido y será ignorado.")

    print(f"Sin repetir: {sin_repetir}")

def ejercicio_13():
    num = float(input("INGRESE UN NUMERO: "))
    if num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    elif  num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    else:
        print(num)

def ejercicio_14():
    texto = input("Ingrese un texto: ")
    vocales = "aeiouAEIOU"
    total = 0

    for letras in texto:
        if letras in vocales:
            total += 1
    print(f"Total de vocales: {total}")

def ejercicio_15():
    texto = input("Ingrese un texto: ")
    texto_invertido = texto[::-1]

    print(texto_invertido)

import re

def validar_contraseña(contraseña):
    patron = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s]).{8,}$'
while True:
    if re.match(patron, contraseña):
        print("Contraseña válida.")
    else:
        print("Contraseña inválida. Debe tener al menos:")
        print("- Una mayúscula")
        print("- Una minúscula")
        print("- Un número")
        print("- Un símbolo especial")
        print("- Al menos 8 caracteres.")
contraseña = input("Ingresa tu contraseña: ")
validar_contraseña(contraseña)












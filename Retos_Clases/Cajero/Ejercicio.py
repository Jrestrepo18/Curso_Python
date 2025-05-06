usuario = {}
c= 0
while True:
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: : ")
    correo =  (input("correo: "))

    c = c + 1
    usuario[c] = {
        "nombre": nombre,
        "apellido:": apellido,
        "correo": correo
    }

    continuar  = int(input("Desea continiar 1.si 2.no "))

    if continuar != 1:
        break
print(usuario)


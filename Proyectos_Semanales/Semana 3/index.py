#Añadir productos:
#Producto definido por nombre, precio y cantidad.
#crecer dinamicamente.

#consultar productor:
#Buscar producto por nombre y obtener detalles precio y cantidad disponible.
#Siel producto no esta, se debe hacer validacion.abs

#Eiminar productos
#ELiminar productos de forma segura.abs

#Calcular el valor toatal del inventario.
#Valor total de los productos en el inventario.
#Utilizar una funcion anonima lambda para el calculo.abs

#Almacenar productos en un diccinario
#EL nombre debe ser la clave y la cantidad y el precio deben ser los valores

#Debe ser interactivo.
from funciones import *
products = {}


print("---------- Sistema de gestión de inventarios ----------")
print("1. Añadir producto.")
print("2. Consultar productos.")
print("3. Actualizar precios.")
print("4. Eliminar productos.")
print("5. Valor total del inventario.")
print("6. salir.")

products = {}

while True:
    op = int(input("\nIngrese una opcion valida: "))
    
    if op == 1:
        back_product = True
        add_product()
    elif op == 2:
        consult_products()
    elif op == 5:
        print("\nSaliste del sistema.")
    else:
        print("Opcion no valida.")






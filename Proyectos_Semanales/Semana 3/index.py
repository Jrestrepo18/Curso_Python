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
print("\n\033[33m---------- Sistema de gestión de inventarios ----------\033[0m\n")
while True:
    print("1. Añadir producto.")
    print("2. Consultar productos.")
    print("3. Actualizar precios.")
    print("4. Eliminar productos.")
    print("5. Valor total del inventario.")
    print("6. salir.")

    try:
        op = int(input("\n\033[32mIngrese una opcion valida:\033[0m "))
    except ValueError:
        print("\033[\n31mIngrese una OPCION valida.\033[0m")
        continue

    if op == 1:
        main(add_product)
    elif op == 2:
        main(consult_products)
    elif op == 3:
        main(update_products)
    elif op == 4:
        main(delete_products)
    elif op == 6:
        print("Has salido del sistema de inventarios... ¡Hasta Luego!")
        break
    else:
        print("\nOpcion no valida.")







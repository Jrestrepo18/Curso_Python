
from inventory import *

add_initial_products()

# MAIN
print("\n\033[34m---------- Sistema de gestión de inventarios ----------\033[0m\n")
while True:
    print(products)
    print("1. Añadir producto.")
    print("2. Consultar productos.")
    print("3. Actualizar precios.")
    print("4. Eliminar productos.")
    print("5. Valor total del inventario.")
    print("6. salir.")

    try:
        op = int(input("\nIngrese una opcion valida:"))
    except ValueError:
        print("\n\033[93mIngrese una OPCION valida.\033[0m")
        continue
    
    # Functions are called when you check an option.
    match op:
        case 1:
            main(add_product)
        case 2:
            main(consult_products)
        case 3:
            main(update_products)
        case 4:
            main(delete_products)
        case 5:
            inventory()
            input("Precione ENTER para volver a l menu ")
        case 6:
            print("\033[92m======================================\033[92m")
            print("\033[92mHas salido del sistema...¡Hasta luego!\033[0m")
            print("\033[92m======================================\033[92m")
            break

            










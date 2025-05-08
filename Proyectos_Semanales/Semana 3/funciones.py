products = {}
def bucle(pedir_dato):
    while True:
        try:
            pedir_dato()  # Ejecuta la función que tú pasas como argumento

        except ValueError:
            print(" Ingrese un valor válido.")
            continue

        while True:
            salir_menu = input("\n¿Desea agregar otro dato? S(si) - N(no): ").lower()
            if salir_menu == "s":
                break  # Repite el bucle
            elif salir_menu == "n":
                return  # Sale de la función
            else:
                print("Por favor, ingrese una opción válida (S / N)")

def add_product():
    back_product = True
    while back_product:
        print("\n Ingrese productos \n")
        while True:
            try:
                name_product = str(input("\nIngrese nombre del producto: "))
                if not name_product.isalpha():
                    print("El nombre del prodructo no puede tener numero, ni caracteres especiales. ")
                else:
                    break
            except ValueError:
                print("Valor invalido. ")
        
        while True:
             try:  
                price_product = float(input("\nIngrese el precio del producto: "))
                if  price_product < 0:
                    print("Valor no valido")
                else:
                     break
             except ValueError:
                  print("Valor invalido. ")
        while True:
             try:
                amount_product = float(input("\nIngrese cantidad de productos:"))
                if amount_product < 0:
                    print("Valor no valido.")
                else:
                     break
             except ValueError:
                  print("Valor invalido. ")

        products[name_product] = {
            "amount" :price_product,
            "price" : price_product 
        }

        print("="*25)
        print("PRODUCTO AGREGADO CON EXITO.")
        print("="*25)

def consult_products():
    if not products:
        print("\n---------- Producto no existente en el inventario. -----------\n")
    else:
        print("\n------ INVENTARIO. ------\n")
        print(f"{'NOMBRE':<20} {'CANTIDAD':<20} {'PRICE':<30}")
        print("-" * 70)
        for name_product, datos in products.items():
            print(f"{name_product:<20} {datos['amount']:<20} {datos['price']:<30}")
        print("-" * 70)
        
        back_product = False

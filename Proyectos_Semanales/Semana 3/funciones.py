products = {}

def main(funcion):
    while True:
        funcion()

        while True:
            exit_menu = input("\n\033[32m¿Desea continuar o regrear al menu? S(si) - N(no):\033[0m ").lower()
            if exit_menu == "s":
                break  
            elif exit_menu == "n":
                return 
            else:
                print("\033[31mPor favor, ingrese una opción válida (S / N)\033[0m")

def add_product():
    print("\n\033[33mIngrese productos al inventario\n\033[0m")

    while True:
        try:
            name_product = str(input("Ingrese nombre del producto: "))
            if not name_product.isalpha():
                print("\033[31mEl nombre del prodructo no puede tener numero, ni caracteres especiales.\033[0m")
            else:
                break
        except ValueError:
            print("\033[31mValor invalido.\033[0m")
    
    while True:
            try:  
                price_product = float(input("Ingrese el precio del producto: "))
                if  price_product < 0:
                    print("\033[\n31m---------- Valor invalido. ----------\033[0m\n")
                else:
                        break
            except ValueError:
                print("\033[\n31m---------- Valor invalido. ----------\033[0m\n")
    while True:
        try:
            amount_product = float(input("Ingrese cantidad del producto: "))
            if amount_product < 0:
                print("\n\033[31m---------- Valor no valido. ----------\033[0m\n")
            else:
                    break
        except ValueError:
            print("\n\033[31m---------- Valor invalido. ----------\033[0m\n")

    products[name_product] = {
        "amount" :amount_product,
        "price" : price_product 
    }

    print("="*30)
    print(f"\033[32mEL producto fue agragado con exito:\033[0m \nNombre del producto: {name_product} \nCantidad del producto: {amount_product} \nValor del producto: {price_product}")
    print("="*30)

def consult_products():
    if not products:
        print("\n\033[31m---------- Producto no existente en el inventario. -----------\n\033[0m")
    else:
        print("\n\033[33m----------------------------- INVENTARIO. -----------------------------\033[0m\n")
        print(f"{'NOMBRE':<20} {'CANTIDAD':<20} {'PRECIO':<30}")
        print("-" * 70)
        for name_product, datos in products.items():
            print(f"{name_product:<20} {datos['amount']:<20} {datos['price']:<30}")
        print("-" * 70)

def update_products():
    print("\n\033[33m---------- Actualizar Precio producto. -----------\033[0m\n")
    while True:
        update_products = input("\nIngrese nombre del producto que desea actulizar: ")
        if update_products not in products:
            print("\n\033[31m---------- Producto no registrado. ----------\033[0m\n")
            #input("Presione ENTER para ingresar un valor valido")
        else:
            new_price = input("Ingrese nuevo precio: ")
            products[update_products]["price"] = new_price
            print(f"\n\033[32Precio actulizado:\033[0m \nNombre del producto: {update_products} \nPrecio actulizado: {new_price}")
            break
        
def delete_products():
    print("\n\033[33m---------- Eliminar prducto. -----------\033[0m\n")
    while True:
        delete_products = input("Ingrese el nombre del producto que sea eliminar: ")
        if delete_products not in products:

            print("\n\033[31m---------- Producto no registrado. ----------\033[0m\n")
        elif delete_products in products:
            del products[delete_products]
            print(f"\n{delete_products} a sido eliminado con exito. ")
            break
    
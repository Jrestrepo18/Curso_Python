
products  = {
    "arroz" :{
        "amount" : 3,
        "price" : 3000
    },
     "sal" : {
        "amount" : 2,
        "price" : 1500
    },
    "pescado" :{
        "amount" : 10,
        "price" : 1000
    },
    "coco" :{
        "amount" : 8,
        "price" : 20000
    },
    "platano" :{
        "amount" : 1,
        "price" : 20000
    }
}
# Enter 5 products to access the system menu.
def add_initial_products():
    print("\n\033[34m--- Ingrese 5 productos para iniciar el programa. ---\033[0m")
    for i in range(5):
        print(f"\nProducto #{i + 1}")
        name = input("Nombre del producto: ").strip()
        while name in products:
            print("\033[31mEse producto ya existe. Ingrese un nombre diferente.\033[0m")
            name = input("Nombre del producto: ").strip()

        try:
            amount = int(input("Cantidad disponible: "))
            price = float(input("Precio unitario: "))
        except ValueError:
            print("\033[31mError: Ingrese valores numéricos válidos.\033[0m")
            return

        products[name] = {'amount': amount, 'price': price}
    print("\n\033[32mProductos ingresados correctamente.\033[0m")

# Function that allows the user to be asked if they want to continue doing the same action or return to the menu.
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

# This function allows you to enter products into the inventory and validates that the user entered the correct information.
def add_product():
    print("\n\033[34mIngrese productos al inventario\n\033[0m")
    while True:
        try:
            name_product = str(input("Ingrese nombre del producto: "))
            if not name_product.isalpha():
                print("\n\033[93mEl nombre del prodructo no puede tener numero, ni caracteres especiales.\033[0m\n")
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
    print(f"\033[32mEL producto fue agragado con exito:\033[0m \nNombre del producto: {name_product} \nCantidad del producto: {amount_product} \nValor del producto: {price_product:,.2f}")
    print("="*30)

# This function allows you to query products, validating that they are in inventory.
def consult_products():
    if not products:
        print("\n\033[93m---------- El inventario está vacío. -----------\033[93m\n")
    product_name = input("\n\033[34mIngrese el nombre del producto que desea buscar:\033[34m ").strip().lower()

    found = False
    for name_product, datos in products.items():
        if name_product.lower() == product_name:
            cantidad = datos['amount']
            precio = datos['price']
            total_value = cantidad * precio
            price_formatted = "${:,.2f}".format(precio)
            total_formatted = "${:,.2f}".format(total_value)

            print("\n\033[33m------------------- PRODUCTO ENCONTRADO -------------------\033[0m\n")
            print(f"{'NOMBRE':<20} {'CANTIDAD':<10} {'PRECIO UNITARIO':<20} {'VALOR TOTAL':<20}")
            print("-" * 70)
            print(f"{name_product:<20} {cantidad:<10} {price_formatted:<20} {total_formatted:<20}")
            print("-" * 70)
            found = True
            break

    if not found:
        print("\n\033[31m---------- Producto no existente en el inventario. -----------\033[0m")

# This function allows you to update products, validating that they are in inventory.
def update_products():
    print("\n\033[34m---------- Actualizar Precio producto. -----------\033[0m\n")
    update_products = input("\nIngrese nombre del producto que desea actulizar: ")
    if update_products not in products:
        print("\n\033[31m---------- Producto no registrado. ----------\033[0m\n")
    else:
        while True:
            new_price = input("Ingrese nuevo precio: ")
            if new_price.isdigit():
                new_price = int(new_price)
                products[update_products]["price"] = new_price
                print(f"\n\033[32Precio actulizado:\033[0m \nNombre del producto: {update_products} \nPrecio actulizado: {new_price:,.2f}")
                break
            else:
                print("\n\033[93mEl precio del producto debe ser un numero positivo\n\033[0m")

# This function allows you to delet products, validating that they are in inventory.
def delete_products():
    print("\n\033[34m---------- Eliminar prducto. -----------\033[34m\n")
    while True:
        delete_products = input("Ingrese el nombre del producto que sea eliminar: ")
        if delete_products not in products:
            print("\n\033[31m---------- Producto no registrado. ----------\033[0m\n")
        elif delete_products in products:
            del products[delete_products]
            print(f"\n{delete_products} a sido eliminado con exito. ")
            break

# This function allows you to view the inventory and its total.
def inventory():
    print("\n\033[34m----------------------------- INVENTARIO. -----------------------------\033[0m\n")
    print(f"{'NOMBRE':<20} {'CANTIDAD':<10} {'PRECIO UNITARIO':<20} {'VALOR TOTAL':<20}")
    print("-" * 70)
    for name_product, datos in products.items():
        cantidad = datos['amount']
        precio = datos['price']
        total_value = cantidad * precio
        price_formatted = "${:,.2f}".format(precio)
        total_formatted = "${:,.2f}".format(total_value)
        print(f"{name_product:<20} {cantidad:<10} {price_formatted:<20} {total_formatted:<20}")
    print("-" * 70)

    total_inventory = lambda i: i ["amount"] * i["price"]
    calculate_total_inventory = sum(total_inventory(i) for i in products.values())
    formatted_total = "${:,.2f}".format(calculate_total_inventory)
    print(f"\n\033[92mTotal inventatio: {formatted_total}\n\033[0m")


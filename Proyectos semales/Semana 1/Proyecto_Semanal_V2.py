producto=[]

productos=[]

back_product=True

continuar=True
total_generado=0

while back_product:
        
        print("\n Ingrese productos \n")

        nom_producto=str(input("\nIngrese nombre del producto: "))

        precio_producto=float(input("\nIngrese el precio del producto: "))
        if precio_producto < 0:
            print("Valor no valido")
            continue

        cant_product=int(input("\nIngrese cantidad de productos:"))
        if cant_product < 0:
            print("Valor no valido.")
            continue

        porcet_descuento=int(input("\nIngrese el descuento: "))
        if not 0 <= porcet_descuento <=100:
            print("Valor no valido.")
            continue
        
        

        producto=([nom_producto,precio_producto,cant_product,porcet_descuento])
        productos.append(producto)

       

        print("\n-------------------------------------")
        salir_menu=input("Desea agregar mas productos S(Si) - N(No)")
        print("\n-------------------------------------")

        if salir_menu.upper() == "N":
            back_product = False
            print("\nFactura Generada")

for producto in productos:
        sub_total=producto[1] * producto[2]
        descuento=(sub_total*producto[3])/100
        total=sub_total-descuento
        total_generado += total
        print(f"\nProducto: {producto[0]} \nPrecio: {producto[1]} \nCantidad: {producto[2]} \nDescuento: {producto[3]}% \nTotal: {total:.3f}\n")

        print(F"Total: {total_generado}")
        print("----------------------------------------------")


print("Feliz dia.")









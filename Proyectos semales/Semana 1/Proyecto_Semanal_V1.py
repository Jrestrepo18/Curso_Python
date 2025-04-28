nom_producto=str(input("Ingrese el nombre del producto: "))


while True:
    try:
        precio_unitario=int(input("Ingrese el precio del prodcuto: "))
        if (precio_unitario < 0):
            print("Digite un valor valido")
        else:
            break
    except ValueError:
        print("Ingrese un valor valido.")


while True:
    try:
        cantidad_productos=int(input("Ingrese la cantidad de productos: "))
        if cantidad_productos < 0:
            print("Ingrese un valor valido")
        else:   
            break
    except ValueError:
        print("Ingrese un valor valido.")

while True:
    try:
        porcet_descuento=int(input("Ingrese el descuento: "))
        if not 0 <= porcet_descuento <= 100:
            print("Descuento invalido")
        else:
            break
    except ValueError:
        print("Ingrese un valor valido.")

##Se hacen todas las operaciones necesarias para poder dar el subtotal y el total con el descuento.

sub_total=precio_unitario * cantidad_productos
descuento=(sub_total*porcet_descuento)/100
total=sub_total-descuento


print(f"{nom_producto} tiene un precio de {sub_total} y con el descuento seria un total de {total}")





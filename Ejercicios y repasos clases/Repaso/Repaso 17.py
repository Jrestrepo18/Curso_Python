nombres = ["ana", "maria", "jose", "luis", "marta", "ana"]  

nombres_buscar = input("Ingrese nombre a buscar: ")

cantidad = nombres.count(nombres_buscar)
print(f"El nombre {nombres_buscar} se repite {cantidad} veces en la lista.")

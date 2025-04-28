frutas = [mango, piña, aguacate]

eliminadar = input("¿Qué fruta quieres eliminar?")

if eliminadar in frutas:
    frutas.remove(eliminadar)
    print("La fruta ha sido eliminada")
else:
    print("La fruta no está en la lista")

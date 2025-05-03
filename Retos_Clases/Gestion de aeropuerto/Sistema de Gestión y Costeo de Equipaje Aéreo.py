usurios={}

id_usurio = 1

print("\n-------------------- Bienvenido al Sistema de Gestión y Costeo de Equipaje Aéreo ✈️--------------------\n")
nombre_usurio = input("Ingrese su nombre: ")
tipo_viaje = input("Tipo de viaje 1) nacional / 2) internacional: ")
peso_equipaje = float(input("Peso de su equipaje: "))
equipaje_mano = input("¿Lleva equipaje de mano S(si) - N(no)")
fecha_viaje = input("Fecha del viaje: ")

op = input("\Ingrese una opcion: ")

usurios[id_usurio] = {
    "nombre":nombre_usurio,
    "viaje":tipo_viaje,
    "peso":peso_equipaje,
    "equipaje_mano":equipaje_mano,
    "fecha_viaje":fecha_viaje

}

usurios
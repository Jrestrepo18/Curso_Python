usurios={}

id_usurio = 1

print("\n-------------------- Bienvenido al Sistema de Gestión y Costeo de Equipaje Aéreo ✈️--------------------\n")
nombre_usurio = input("Ingrese su nombre: ")
tipo_viaje = input("\nTipo de viaje 1) nacional / 2) internacional: ")
if tipo_viaje == "nacional":
    costo_base= 240000
    print("\nCosto del viaje 230.000.")
elif tipo_viaje == "internacional":
    costo_base= 4200000
    print("\nCosto del viaje 4.200.000.")
else:
    print("\nViaje no disponible.")

peso_equipaje = float(input("Peso de su equipaje: "))
if peso_equipaje <= 20:
    print("\nValor a pagar es de $50.000")
    costo_equipaje = 50.000
elif peso_equipaje <= 30:
    print("\nValor a pagar es de $70.000")
    costo_equipaje = 70.000
elif peso_equipaje < 49:
    print("\nValor a pagar es de $110.000")
    peso_equipaje =110.000
else:
    print("\nNo admitido, debe cancelar o viajar sin equipaje.")

equipaje_mano = input("¿Lleva equipaje de mano S(si) - N(no)").lower()
if equipaje_mano == "s":
    max_permitido = input("Peso equipaje de mano: ")
    if max_permitido <= 13:
        print("Equipaje de mano permitido.")
    else:
        print("Equipaje de mano permitido, puede abordar el avion sin equipaje de mano.")
elif equipaje_mano == "n":
    print("Sin equipaje de mano.")
else:
    print("Respuesta no permitida")

total_pajar = costo_base + costo_equipaje

fecha_viaje = input("Fecha del viaje: ")

usurios[id_usurio] = {
    "nombre":nombre_usurio,
    "viaje":tipo_viaje,
    "peso":peso_equipaje,
    "equipaje_mano":equipaje_mano,
    "fecha_viaje":fecha_viaje

}


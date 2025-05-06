from datetime import datetime

usuarios = {}
contador_id = 1

while True:
    print("\n-------------------- Bienvenido al Sistema de Gestión y Costeo de Equipaje Aéreo ✈️--------------------")
    print("1. Registrar pasajero.")
    print("2. Ver reportes.")
    print("3. Consultar por ID ")
    print("4. Salir.")
    
    op = int(input("\nIngrese una opción: "))
    print("-" * 50)

    if op == 1:
        print("\nIngrese su información para el viaje.")
        while True:
            nombre_usuario = input("\nIngrese su nombre: ")
            if nombre_usuario.replace(" ", "").isalpha():
                break
            else:
                print("\033[31mEl nombre no puede contener números ni caracteres especiales.\033[0m")
        
        while True:
            print("\nSeleccione el destino de su viaje:")
            tipo_viaje = int(input("\nTipo de viaje 1) nacional / 2) internacional: "))
            if tipo_viaje == 1:
                costo_base = 230000
                destino = "Bogotá - Medellín"
                print("\nBogotá - Medellín")
                print("Costo del viaje 230.000.")
                break
            elif tipo_viaje == 2:
                costo_base = 4200000
                destino = "Bogotá - España"
                print("\nBogotá - España")
                print("\nCosto del viaje 4.200.000.")
                break
            else:
                print("\n\033[31mOpción no válida, por favor seleccione 1 o 2.\033[0m")

        while True:
            try:
                opcion = input("\n¿Llevas equipaje principal? S(si) - N(no)").lower()

                if opcion == "s":
                    equipaje_principal = float(input("Ingrese el peso de su equipaje principal en kg: "))
                    if equipaje_principal <= 0:
                        print("Ingrese un valor válido.")
                        continue
                    if equipaje_principal <= 20:
                        print("\nValor a pagar es de $50.000")
                        costo_equipaje = 50000
                        estado_equipaje = "Equipaje permitido"
                    elif equipaje_principal <= 30:
                        print("\nValor a pagar es de $70.000")
                        costo_equipaje = 70000
                        estado_equipaje = "Equipaje permitido"
                    elif equipaje_principal <= 49:
                        print("\nValor a pagar es de $110.000")
                        costo_equipaje = 110000
                        estado_equipaje = "Equipaje permitido" 
                    else:
                        print("\033[31mNo admitido, debe cancelar o viajar sin equipaje.\033[0m")
                        equipaje_principal = 0
                        costo_equipaje = 0
                        estado_equipaje = "Equipaje no permitido"
                    break
                elif opcion == "n":
                    equipaje_principal = 0
                    costo_equipaje = 0
                    estado_equipaje = "No lleva equipaje principal."
                    print("Sin equipaje principal.")
                    break
                else:
                    print("\033[31mIngrese una opción válida.\033[0m")
            except ValueError:
                print("\033[32mIngrese un valor válido.\033[0m")

        equipaje_mano = input("\n¿Lleva equipaje de mano S(si) - N(no)").lower()
        if equipaje_mano == "s":
            max_permitido = float(input("\nPeso equipaje de mano: "))
            if max_permitido <= 13:
                print("\nEquipaje de mano permitido.")
                estado_equipaje_mano = "Equipaje permitido"
            else:
                print("\nEquipaje de mano no permitido, puede abordar el avión sin equipaje de mano.")
                estado_equipaje_mano = "Equipaje no permitido"
        elif equipaje_mano == "n":
            max_permitido = 0
            estado_equipaje_mano = "No lleva equipaje de mano"
            print("\nSin equipaje de mano.")
        else:
            print("Respuesta no permitida")

        while True:
            try:
                fecha_viaje = input("\nFecha del viaje (formato DD/MM/AAAA): ")
                fecha_viaje = datetime.strptime(fecha_viaje, "%d/%m/%Y").date()
                break
            except ValueError:
                print("Formato de fecha no válido. Por favor, use el formato DD/MM/AAAA.")

        total_pagar = costo_base + costo_equipaje

        id_usuario = "COMP" + str(contador_id).zfill(4)
        usuarios[id_usuario] = {
            "nombre": nombre_usuario,
            "destino": destino,
            "fecha_viaje": fecha_viaje,
            "equipaje_principal": equipaje_principal,
            "costo_equipaje": costo_equipaje,
            "estado_equipaje": estado_equipaje,
            "equipaje_mano": equipaje_mano,
            "peso_equipaje_mano": max_permitido,
            "estado_equipaje_mano": estado_equipaje_mano,
            "total": total_pagar
        }
        contador_id += 1  # Incrementar el contador_id después de cada registro de usuario

        print("-" * 40)
        for id_usuario, datos in usuarios.items():  
            print("\n----- Resumen del viaje -----\n")
            print(f"ID compra: {id_usuario}")
            print(f"Nombre pasajero: {datos['nombre']}")
            print(f"Destino: {datos['destino']}")
            print(f"Fecha del viaje: {datos['fecha_viaje']}")
            print("-" * 40)
            print("Equipaje principal:")
            print(f"Estado del equipaje: {datos['estado_equipaje']}")
            print(f"Peso del equipaje: {datos['equipaje_principal']} kg")
            print(f"Costo del equipaje: {datos['costo_equipaje']}")
            print("-" * 40)
            print(f"Equipaje de mano: {datos['equipaje_mano']}")
            print(f"Estado del equipaje de mano: {datos['estado_equipaje_mano']}")
            print(f"Peso del equipaje de mano: {datos['peso_equipaje_mano']} kg")
            print("-" * 40)
            print(f"Total a pagar: {datos['total']}")   
            print("-" * 40)
            salir_menu = input("\n¿Desea agregar otro pasajero? (S/N): ").lower()
            if salir_menu == "n":
                break  # Rompe este ciclo y vuelve al menú principal
            elif salir_menu != "s":
                print("\033[31mOpción no válida, por favor ingrese S o N.\033[0m")

    elif op == 2:
        total_pasajeros = 0
        total_recaudado = 0
        nacionales = 0
        internacionales = 0

        for datos in usuarios.values():
            total_pasajeros += 1
            total_recaudado += datos["total"]

            if datos["destino"] == "Bogotá - Medellín":
                nacionales += 1
            elif datos["destino"] == "Bogotá - España":
                internacionales += 1

        print(f"Total de pasajeros: {total_pasajeros}")
        print(f"Total recaudado: {total_recaudado}")
        print(f"Pasajeros Nacionales: {nacionales}")
        print(f"Pasajeros Internacionales: {internacionales}")
    
    elif op == 3:
        id_buscar = input("\nIngrese el ID del pasajero: ")
        if id_buscar in usuarios:
            datos = usuarios[id_buscar]
            print(f"\nDatos del pasajero con ID {id_buscar}:")
            print(f"Nombre: {datos['nombre']}")
            print(f"Destino: {datos['destino']}")
            print(f"Fecha de viaje: {datos['fecha_viaje']}")
            print(f"Equipaje principal: {datos['estado_equipaje']}")
            print(f"Peso del equipaje: {datos['equipaje_principal']} kg")
            print(f"Equipaje de mano: {datos['estado_equipaje_mano']}")
            print(f"Peso del equipaje de mano: {datos['peso_equipaje_mano']} kg")
            print(f"Total a pagar: {datos['total']}")
        else:
            print("\033[31mID no encontrado.\033[0m")

    elif op == 4:
        print("¡Hasta luego!")
        break

    else:
        print("\033[31mOpción no válida.\033[0m")

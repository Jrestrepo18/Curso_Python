from datetime import datetime
usurios={}
contador_id = 1

while True:
    print("\n-------------------- Bienvenido al Sistema de Gestión y Costeo de Equipaje Aéreo ✈️--------------------")
    print("\nIngrese su informacion para el viaje.")
    while True:
        nombre_usurio = input("\nIngrese su nombre: ")
        if nombre_usurio.replace(" ", "").isalpha():
            break
        else:
            print("El nombre no puede contener números ni caracteres especiales.")
    
   
    while True:
        try:
            print("\nSeleccione el destino de su viaje:")
            tipo_viaje = int(input("\nTipo de viaje 1) nacional / 2) internacional: "))
        
            if tipo_viaje == 1:
                costo_base= 230000
                print("-"*25)
                destino = "Bogota - Medellin"
                print("\nBogota - Medellin")
                print("Costo del viaje 230.000.")
                print("-"*25)
                break
                
            elif tipo_viaje == 2:
                costo_base= 4200000
                print("-"*25)
                destino = "Bogota - España"
                print("\nBogota - España")
                print("\nCosto del viaje 4.200.000.")
                print("-"*25)
                break
        except ValueError:
            print("Por favor, ingrese un número válido.")   
        else:
            print("\nOpcion no valida, por favor seleccione 1 o 2.")
            

    while True:
        try:
            equipaje_principal = float(input("\nPeso de su equipaje Principal: "))
            if equipaje_principal <= 20:
                print("\nValor a pagar es de $50.000")
                costo_equipaje = 50000
                estado_equipaje = "Equipaje permitido"
                break
            elif equipaje_principal <= 30:
                print("\nValor a pagar es de $70.000")
                costo_equipaje = 70000
                estado_equipaje = "Equipaje permitido"
                break
            elif equipaje_principal < 49:
                print("\nValor a pagar es de $110.000")
                costo_equipaje =110000
                estado_equipaje = "Equipaje permitido"
                break
            else:
                print("\nNo admitido, debe cancelar o viajar sin equipaje.")
                costo_equipaje = 0
                estado_equipaje = "Equipaje no permitido"
                break
        except ValueError:
            print("El peso del equipaje debe ser un número válido.")
          
      
    while True:
        try:
            equipaje_mano = input("\n¿Lleva equipaje de mano S(si) - N(no)").lower()
            if equipaje_mano == "s":
                max_permitido = float(input("\nPeso equipaje de mano: "))
                if max_permitido <= 13:
                    print("\nEquipaje de mano permitido.")
                    print("Puede abordar el avion con su equipaje de mano.")
                    costo_equipaje_mano = 0
                    estado_equipaje_mano = "Equipaje permitido"
                else:
                    print("\nEquipaje de mano permitido, puede abordar el avion sin equipaje de mano.")
                    estado_equipaje_mano = "Equipaje no permitido"
                break

            elif equipaje_mano == "n":
                max_permitido = 0
                costo_equipaje_mano = 0
                estado_equipaje_mano = "No lleva equipaje de mano"
                print("\nSin equipaje de mano.")
                break

            else:
                print("Respuesta no permitida")

        except ValueError:
            print("Ingrese un valor valido.")
    total_pagar = costo_base + costo_equipaje

    while True:
        try:
            fecha_viaje = input("\nFecha del viaje formato DD/MM/AAAA: ")
            fecha_viaje = datetime.strptime(fecha_viaje, "%d/%m/%Y").date()
            break
        except ValueError:
            print("Formato de fecha no válido. Por favor, use el formato DD/MM/AAAA.")

    id_usuarios = "COMP" + str(contador_id).zfill(4)
    usurios[id_usuarios] = {
        "nombre":nombre_usurio,
        "destino":destino,
        "fecha_viaje":fecha_viaje,
        "equipaje_principal":equipaje_principal,
        "costo_equipaje":costo_equipaje,
        "estado_equipaje":estado_equipaje,
        "equipaje_mano":equipaje_mano,
        "peso_equipaje_mano":max_permitido,
        "estado_equipaje_mano":estado_equipaje_mano,
        "total":total_pagar
    }


    print("-" * 40)
    for id_usuarios, datos in usurios.items():  
        print("\n----- Resumen del viaje -----\n")
        print(f"ID compra: {id_usuarios}")
        print(f"Nombre pasajero: {datos['nombre']}")
        print(f"Destino: {datos['destino']}")
        print(f"Fecha del viaje: {datos['fecha_viaje']}")
        print("-" * 40)
        print("Equipaje principal:")
        print(f"Estado del equipaje: {estado_equipaje}")
        print(f"Peso del equipaje: {datos['equipaje_principal']} kg")
        print(f"Costo del equipaje: {datos['costo_equipaje']}")
        print("-" * 40)
        print(f"Equipaje de mano: {datos['equipaje_mano']}")
        print(f"Estado del equipaje de mano: {datos['estado_equipaje_mano']}")
        print(f"Peso del equipaje de mano: {datos['peso_equipaje_mano']} kg")
        print("-" * 40)
        print(f"Total a pagar: {datos['total']}")   
        print("-" * 40)
    while True:
        salir_menu = input("\n¿Desea agregar otro pasajero? (S/N): ").lower()
        if salir_menu == "s":
            break
        elif salir_menu == "n":
            print("-" * 40)
            print("\n¡Buen viaje!")
            print("-" * 40)
            exit()
        else:
            print("Opción no válida. Por favor, ingrese S o N.")

    








        
    


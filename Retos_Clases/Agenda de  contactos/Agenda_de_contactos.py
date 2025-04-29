agenda = {}

back_menu=True

while back_menu:
    print("\n------ Agenda de contcatos ------\n")
    print("1) agregar un nuevo contacto. ")
    print("2) Ver contactos.")
    print("3) Actializar contacto.")
    print("4) Eliminar contacto.")
    print("5) Salir.")

    op = int(input("\nIngrese una opcion: "))

    if op == 1:
    ## Agregar un nuevo contacto: 
        while  True:
            while True:
                nombre_contacto = input("\nNombre del contacto: ")
                if nombre_contacto.replace(" " ,"").isalpha():
                    break
                else:
                    print("El nombre no puede contener numero ni caracteres especiales.")

            while True:
                numero_telefonico = input("\nNumero telefonico: ")
                if numero_telefonico.isdigit():
                    numero_telefonico = int(numero_telefonico)
                    break
                else:
                    print("El numero no puede tener letras ni caracteres especiales.")
        
            while True:
                correo = (input("\nEmail: "))
                if "@" in correo and "." in correo and " " not in correo:
                    break
                else:
                    print("El nombre no puede contener numero ni caracteres especiales.")
                

            
                agenda [nombre_contacto] = {
                    "Telefono:": numero_telefonico,
                    "Email:": correo
                }

                print("="*55)
                print("Contacto agragado existosamente.")
                print("="*55)
            ## Devuelve si desea agregar otro usuario.   
                while True:
                    salir_menu = input("\n¿Desea agregar otro contacto? S(si) - N(no): ").lower()
                    if salir_menu == "s":
                        break  
                    elif salir_menu == "n":
                        break 
                    else:
                        print("Por favor, ingrese una opción válida (S / N)")

                if salir_menu == "n":
                    break  
    elif op == 2:
        if not agenda:
            print("\n----------Agenda vacía -----------\n")
        else:
        ## Muestra contactos en tabla:
            print("\n------ Contactos ------\n")
            print(f"{'Nombre':<20} {'Teléfono':<20} {'Email':<30}")
            print("-" * 48)
            for nombre, datos in agenda.items():
                print(f"{nombre:<20} {datos['Telefono:']:<20} {datos['Email:']:<30}")
            print("-" * 48)

        input("\n Presione ENTER para salir al menu.")

    elif op == 3:
        while True:
        ## Muestra contactos en tabla:
            print("\n------ Contactos ------\n")
            print(f"{'Nombre':<20} {'Teléfono':<20} {'Email':<30}")
            print("-" * 48)
            for nombre, datos in agenda.items():
                print(f"{nombre:<20} {datos['Telefono:']:<20} {datos['Email:']:<30}")
            print("-" * 48)
            
            if not agenda:
                print("\nContacto no registado.")
                continue
        ## Actualiza contactos:
            nombre_actualizar= str(input("\nIngrese el nombre del contacto que desea actualizar: "))
            if nombre_actualizar not in agenda:
                print("\nContacto no registado.")
                input("\nPresione ENTER para buscar nuevamente el usurio. ")
            else:
                print("\n----- Actualice infomacion del Contacto-----\n")
                nuevo_telefono = input("Numero telefonico: ")
                nuevo_email = input("EMail: ")

                agenda[nombre_actualizar]={

                    "Telefono:": nuevo_telefono,
                    "Email:": nuevo_email

                }
            ## Muestra contactos en tabla:
                print("\n----- Contacto Actualizado. -----\n")
                print(f"{'Nombre':<20} {'Teléfono':<20} {'Email':<30}")
                print("-" * 48)
                for nombre, datos in agenda.items():
                    print(f"{nombre:<20} {datos['Telefono:']:<20} {datos['Email:']:<30}")
                print("-" * 48)

            ## Devuelve si desea agregar otro usuario:
                while True:
                    salir_menu = input("\n¿Desea Actualizar otro contacto? S(si) - N(no): ").lower()
                    if salir_menu == "s":
                        break  
                    elif salir_menu == "n":
                        break 
                    else:
                        print("Por favor, ingrese una opción válida (S / N)")

                if salir_menu == "n":
                    break 
    elif op == 4:
        while True:
            try:
            ## Muestra contactos organizados en tabla:
                print("\n----- Contacto Actualizado. -----\n")
                print(f"{'Nombre':<20} {'Teléfono':<20} {'Email':<30}")
                print("-" * 48)
                for nombre, datos in agenda.items():
                    print(f"{nombre:<20} {datos['Telefono:']:<20} {datos['Email:']:<30}")
                print("-" * 48)

            ##Elimina contactos:
                contacto_eliminar = str(input("Ingrese el nombre del usurio que desea eliminar: "))
                if contacto_eliminar in agenda:
                    del agenda[contacto_eliminar]
                
                ## Muestra contactos organizados en tabla:
                    print("\n----- Contactos. -----\n")
                    print(f"{'Nombre':<20} {'Teléfono':<20} {'Email':<30}")
                    print("-" * 48)
                    for nombre, datos in agenda.items():
                        print(f"{nombre:<20} {datos['Telefono:']:<20} {datos['Email:']:<30}")
                    print("-" * 48)
                        
                    print(f"Contacto {contacto_eliminar} a sido eliminado.")

                    ## Devuelve si desea agregar otro usuario:
                    while True:
                        salir_menu = input("\n¿Desea Eliminar otro contacto? S(si) - N(no): ").lower()
                        if salir_menu == "s":
                            break  
                        elif salir_menu == "n":
                                break 
                        else:
                            print("Por favor, ingrese una opción válida (S / N)")

                    if salir_menu == "n":
                            break 
                else: 
                    print("\nNombre de contacto no valido no valido.\n")
            except ValueError:
                print("Ingrese un valor valido.")

    elif op == 5:
        print("\n--------------------------------------------")
        print("Has salido del sistema... ¡Hasta pronto!")
        print("--------------------------------------------\n")
        break

    print("hola")

    print("hola")
        
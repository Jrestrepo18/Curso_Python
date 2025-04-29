agenda = {}

back_menu = True

while back_menu:
    print("\n------ Agenda de Contactos ------\n")
    print("1) Agregar un nuevo contacto.")
    print("2) Ver contactos.")
    print("3) Actualizar contacto.")
    print("4) Eliminar contacto.")
    print("5) Salir.")

    try:
        op = int(input("\nIngrese una opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    if op == 1:
        while True:
            while True:
                nombre_contacto = input("\nNombre del contacto: ")
                if nombre_contacto.replace(" ", "").isalpha():
                    break
                else:
                    print("El nombre no puede contener números ni caracteres especiales.")

            while True:
                numero_telefonico = input("Número telefónico: ")
                if numero_telefonico.isdigit():
                    numero_telefonico = int(numero_telefonico)
                    break
                else:
                    print("El número no puede tener letras ni caracteres especiales.")

            while True:
                correo = input("Email: ")
                if "@" in correo and "." in correo:
                    break
                else:
                    print("Correo no válido. Asegúrese de que contenga '@' y un dominio como '.com'.")

            agenda[nombre_contacto] = {
                "Telefono": numero_telefonico,
                "Email": correo
            }

            print("=" * 55)
            print("Contacto agregado exitosamente.")
            print("=" * 55)

            while True:
                salir_menu = input("\n¿Desea agregar otro contacto? S(si) - N(no): ").lower()
                if salir_menu == "s":
                    break
                elif salir_menu == "n":
                    break
                else:
                    print("Por favor, ingrese una opción válida (S / N).")

            if salir_menu == "n":
                break

    elif op == 2:
        if not agenda:
            print("\n---------- Agenda vacía -----------\n")
        else:
            print("\n------ Contactos ------\n")
            print(f"{'Nombre':<20} {'Teléfono':<20} {'Email':<30}")
            print("-" * 70)
            for nombre, datos in agenda.items():
                print(f"{nombre:<20} {datos['Telefono']:<20} {datos['Email']:<30}")
            print("-" * 70)

        input("\nPresione ENTER para volver al menú.")

    elif op == 3:
        if not agenda:
            print("\nNo hay contactos registrados.")
            continue

        while True:
            print("\n------ Contactos ------\n")
            print(f"{'Nombre':<20} {'Teléfono':<20} {'Email':<30}")
            print("-" * 70)
            for nombre, datos in agenda.items():
                print(f"{nombre:<20} {datos['Telefono']:<20} {datos['Email']:<30}")
            print("-" * 70)

            nombre_actualizar = input("\nIngrese el nombre del contacto que desea actualizar: ")
            if nombre_actualizar not in agenda:
                print("\nContacto no registrado.")
                input("\nPresione ENTER para intentar de nuevo.")
                continue

            nuevo_telefono = input("Nuevo número telefónico: ")
            nuevo_email = input("Nuevo email: ")

            agenda[nombre_actualizar] = {
                "Telefono": nuevo_telefono,
                "Email": nuevo_email
            }

            print("\n----- Contacto Actualizado -----\n")
            print(f"{'Nombre':<20} {'Teléfono':<20} {'Email':<30}")
            print("-" * 70)
            for nombre, datos in agenda.items():
                print(f"{nombre:<20} {datos['Telefono']:<20} {datos['Email']:<30}")
            print("-" * 70)

            while True:
                salir_menu = input("\n¿Desea actualizar otro contacto? S(si) - N(no): ").lower()
                if salir_menu in ["s", "n"]:
                    break
                else:
                    print("Por favor, ingrese una opción válida (S / N).")

            if salir_menu == "n":
                break

    elif op == 4:
        if not agenda:
            print("\nNo hay contactos para eliminar.")
            continue

        while True:
            print("\n------ Contactos ------\n")
            print(f"{'Nombre':<20} {'Teléfono':<20} {'Email':<30}")
            print("-" * 70)
            for nombre, datos in agenda.items():
                print(f"{nombre:<20} {datos['Telefono']:<20} {datos['Email']:<30}")
            print("-" * 70)

            contacto_eliminar = input("Ingrese el nombre del contacto que desea eliminar: ")
            if contacto_eliminar in agenda:
                del agenda[contacto_eliminar]
                print(f"\nContacto '{contacto_eliminar}' ha sido eliminado.")

                if agenda:
                    print("\n------ Contactos Restantes ------\n")
                    print(f"{'Nombre':<20} {'Teléfono':<20} {'Email':<30}")
                    print("-" * 70)
                    for nombre, datos in agenda.items():
                        print(f"{nombre:<20} {datos['Telefono']:<20} {datos['Email']:<30}")
                    print("-" * 70)
                else:
                    print("\nLa agenda está vacía.")
            else:
                print("Contacto no encontrado.")

            while True:
                salir_menu = input("\n¿Desea eliminar otro contacto? S(si) - N(no): ").lower()
                if salir_menu in ["s", "n"]:
                    break
                else:
                    print("Por favor, ingrese una opción válida (S / N).")

            if salir_menu == "n":
                break

    elif op == 5:
        print("\n--------------------------------------------")
        print("Has salido del sistema... ¡Hasta pronto!")
        print("--------------------------------------------\n")
        break
    else:
        print("Opción inválida. Por favor, elija entre 1 y 5.")

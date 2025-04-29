bibliotecas = {}

c = 100

back_menu=True

while back_menu:
    print("Bienvenido al sistema\n")
    print("1) agregar un nuevo libro. ")
    print("2) Ver biblioteca.")
    print("3) Actializar libro con ID.")
    print("4) Eliminar un libro con ID.")
    print("5) Salir.")

    op = int(input("\nIngrese una opcion: "))


    if op == 1:
        while  True:
            try:
                nombre_libro = input("\nIngrese nombre del libro: ")
                nombre_autor = input("\nIngrese nombre del autor: ")
                año_publicacion = int(input("\nIngrese año de publucacion: "))

                c = c +1
                bibliotecas[c] = {
                    "Nombre libro:": nombre_libro,
                    "Nombre del autor:": nombre_autor,
                    "Año de publicacion:": año_publicacion
                }

                print("="*55)
                print(f"El libro {nombre_libro} se agregado correctamente con el ID: {c}")
                print("="*55)
            except ValueError:
                print("Ingrese un valor valido ")

            while True:
                salir_menu = input("\n¿Desea agregar más libros? S(si) - N(no): ").lower()
                if salir_menu == "s":
                    break  
                elif salir_menu == "n":
                    break 
                else:
                    print("Por favor, ingrese una opción válida (S / N)")

            if salir_menu == "n":
                break  

    elif op == 2:
            if not bibliotecas:
                print("\n------ Biblioteca vacía -----\n")
            else:
                print("\n----- Libros en la Biblioteca -----\n")
                print(f"{'ID':<6} {'Nombre del libro':<30} {'Nombre del autor':<25} {'Año de publicación':<6}")
                print("-" * 80)
                for c, datos in bibliotecas.items():  
                    print(f"{c:<6} {datos['Nombre libro:']:<30} {datos['Nombre del autor:']:<25} {datos['Año de publicacion:']:<6}")
                print("-" * 80)
                input("\nPresione ENTER para regresar al menú")
          
            

    elif op == 3:
       
        while True:
            print("\n----- Seleccione el libro que desea actializar -----\n")
            print(f"{'ID':<6} {'Nombre del libro':<30} {'Nombre del autor':<25} {'Año de publicación':<6}")
            print("-" * 80)
            for c, datos in bibliotecas.items():  
                print(f"{c:<6} {datos['Nombre libro:']:<30} {datos['Nombre del autor:']:<25} {datos['Año de publicacion:']:<6}")
            print("-" * 80)
    
            id_libro = int(input("Ingrese el ID del libro que desea actualizar: "))
            if id_libro not in bibliotecas:
                print("\nID no registado.")
            else:
                print("\n----- Actualice infomacion del libro -----\n")
                nuevo_nombre = input("Ingrese el nombre del libro: ")
                nuevo_autor = input("Ingrese el autor del libro: ")
                nuevo_año = input("Ingrese el año de publicacion del libro: ")
         
      

                bibliotecas[id_libro]={
                    "Nombre libro:": nuevo_nombre,
                    "Nombre del autor:": nuevo_autor,
                    "Año de publicacion:": nuevo_año

                }
                print("\n----- Libro Actualizado. -----\n")
                print(f"{'ID':<6} {'Nombre del libro':<30} {'Nombre del autor':<25} {'Año de publicación':<6}")
                print("-" * 80)
                for c, datos in bibliotecas.items():  
                    print(f"{c:<6} {datos['Nombre libro:']:<30} {datos['Nombre del autor:']:<25} {datos['Año de publicacion:']:<6}")
                print("-" * 80)
        

                while True:
                    salir_menu = input("\n¿Desea agregar más libros? S(si) - N(no): ").lower()
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
                print(f"\nEl libro {nombre_libro} con el ID {c} a sido eliminado.\n")
                print(f"{'ID':<6} {'Nombre del libro':<30} {'Nombre del autor':<25} {'Año de publicación':<6}")
                print("-" * 80)
                for c, datos in bibliotecas.items():  
                    print(f"{c:<6} {datos['Nombre libro:']:<30} {datos['Nombre del autor:']:<25} {datos['Año de publicacion:']:<6}")
                print("-" * 80)
                id_eliminar = int(input("Ingrese el ID del libro que desea eliminar: "))
                if id_eliminar in bibliotecas:
                    del bibliotecas[id_eliminar]
                    print("="*60)
                    print("\n----- Libros en la Biblioteca -----\n")
                    print(f"{'ID':<6} {'Nombre del libro':<30} {'Nombre del autor':<25} {'Año de publicación':<6}")
                    print("-" * 80)
                    for c, datos in bibliotecas.items():  
                        print(f"{c:<6} {datos['Nombre libro:']:<30} {datos['Nombre del autor:']:<25} {datos['Año de publicacion:']:<6}")
                    print("-" * 80)

                    while True:
                        salir_menu = input("\n¿Desea agregar más libros? S(si) - N(no): ").lower()
                        if salir_menu == "s":
                            break  
                        elif salir_menu == "n":
                            break 
                        else:
                            print("Por favor, ingrese una opción válida (S / N)")

                    if salir_menu == "n":
                        break 
                    
                else:
                    print("Ingrese ID Valido. ")
            except ValueError:
                print("Ingrese un ID valido.")
                
                
    elif op == 5:
        print("Saliste del menu... Hasta luego.")
        back_menu = False


        print("hola")

    
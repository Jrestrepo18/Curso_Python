
students = {}
id_student = 1000  


def agregar_estudiante():
    global id_student  
    while True:
        name_student = input("Ingrese el nombre del estudiante: ")
        age_student = int(input("Ingrese la edad del estudiante: "))
        note_student = float(input("Ingrese la nota del estudiante: "))

        id_student += 1
        id_student = "STU" + str(id_student).zfill(4)
        
        students[id_student] = {
            "name": name_student,
            "age": age_student,
            "note_student": note_student
        }

        print(f"Estudiante agregado con éxito: {id_student}.")
  
        salir_menu = input("\n¿Desea agregar otro estudiante? S(si) - N(no): ").lower()
        if salir_menu == "n":
            break
        elif salir_menu != "s":
            print("Por favor, ingrese una opción válida (S / N).")

def menu():
    print("Bienvenido al sistema de gestión de estudiantes.")
    print("\nIngrese una opción de 1 - 6")
    print("\n1. Agregar un estudiante.")
    print("2. Buscar un estudiante por ID.")
    print("3. Actualizar información del estudiante.")
    print("4. Eliminar estudiante.")
    print("5. Informe general de estudiantes.")

    while True:
        op = int(input("Ingrese una OPCION: "))

        if op == 1:
            agregar_estudiante()
        elif op == 2:
            print("Opción 2 seleccionada.")
            
        elif op == 3:
            print("Opción 3 seleccionada.")
          
        elif op == 4:
            print("Opción 4 seleccionada.")
            
        elif op == 5:
            print("Opción 5 seleccionada.")
           
        else:
            print("Opción no válida. Intente nuevamente.")


menu()

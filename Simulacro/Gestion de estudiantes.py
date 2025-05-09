from funciones import *

students = {}
id_counter = 1000

def op_1():
    while True:
        try:
            name_student= input("\nIngrese nombre del estudiante: ")
            age_student = int(input("\nIngrese la edad del estudiante: "))
            note = input("\nIngrese su nota entre (0.0 - 5.0): ")
           
            id_counter =+ 1
            id_usuario = "STU" + str(id_counter).zfill(4)
            students[id_usuario] = {

                "name_student" : name_student,
                "age_student" : age_student,
                "note" : note
            }

            print("="*55)
            print(f"El estudiante {name_student} se agregado correctamente con el ID: {id_usuario}")
            print("="*55)
        except ValueError:
            print("Ingrese un valor valido ")

        while True:
            salir_menu = input("\n¿Desea agregar otro estudiante? S(si) - N(no): ").lower()
            if salir_menu == "s":
                break  
            elif salir_menu == "n":
                break 
            else:
                print("Por favor, ingrese una opción válida (S / N)")

        if salir_menu == "n":
            break
def op_2():
    id_search = input("Ingrese el ID del estudiante que desea buscar: ")
    if id_search not in students:
        print("Estudiante no existente.")
    elif id_search in students:
        print(f"ID: {id_search}")
        print(f"Nombre del estudiante: {students[id_search]['name_student']}")
        print(f"Edad: {students[id_search]['age_student']}")
        print(f"Nota: {students[id_search]['note']}")
    else:
        print("Estudiante no encontrado.")

def op_3():
    update_student = input("Ingrese el ID del estudiante que desea Actulizar")
    if update_student not in students:
        print("\nID no registado.")
    else:
        print("\n----- Actualice infomacion del estudiante.-----\n")
        new_age = input("Ingrese la edad del estudiante: ")
        new_note = float(input("Ingrese la nota del estudiante: "))

        students[update_student]={
            "age_student" : new_age,
            "note" : new_note

                }
def op_4():
    while True:
        try:
            id_delet = input("Ingrese el ID del estudiante que desea eliminar: ")
            if id_delet not in students:
                print("Estudiante no registrado.")  
            elif id_delet in students:
                del students[id_delet]

            print("\nEstudiante eliminado con exito.")

            while True:
                salir_menu = input("\n¿Desea Eliminar otro estudiante? S(si) - N(no): ").lower()
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
            op_1()
        elif op == 2:
            op_2()
        elif op == 3:
            op_3()
        elif op == 4:
            op_4()
            
        elif op == 5:
            print("Opción 5 seleccionada.")
            
        else:
            print("Opción no válida. Intente nuevamente.")
            print("Opcion no valida.")

menu()






            









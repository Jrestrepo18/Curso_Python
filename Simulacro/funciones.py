
students = {
    1010 :{
        "full_name" : "Roberto",
        "age" : 30,
        "note" : 5.0
    },
    1011 :{
        "full_name" : "Tomas",
        "age" : 35,
        "note" : 4.0
    },
    1012 :{
        "full_name" : "Daniel",
        "age" : 25,
        "note" : 2.3
    },
    1013 :{
        "full_name" : "Daniela",
        "age" : 20,
        "note" : 2.5
    },
    1014 :{
        "full_name" : "Fredy",
        "age" : 20,
        "note" : 3.0
    }
}

def main(funcion):
    while True:
        funcion()
        while True:
            exit_menu = input("\n\033[32m¿Desea continuar o regrear al menu? S(si) - N(no):\033[0m ").lower()
            if exit_menu == "s":
                break  
            elif exit_menu == "n":
                return 
            else:
                print("\033[31mPor favor, ingrese una opción válida (S / N)\033[0m")


def aggregate_student():
    print("-------------------- Agregar estudiante --------------------")
    id_student = int(input("Ingrese el ID del estudiante: "))
    if id_student in students:
        
        print("\n\033[93m El ID ya se encuentra registado. \033[0m\n")
    else:
        full_name = input("Ingrese el nombre del estudiane: ")
        age = int(input("Ingrese la edad del estudiante: "))
        note = float(input("Ingrese la nota del estudiante: "))
    
        students[id_student] = {
            "full_name" : full_name,
            "age" : age,
            "note" : note
            
        }
                
def search_students():
    print("-------------------- Buscar estudiante --------------------")
    id_search = int(input("Ingrese el ID del estudiante que desea buscar: "))
    if id_search not in students:
        print("\n\033[93mEl estudiante no se encuentre en el sistema.\033[0m\n")
    elif id_search in students:
        print(f"ID: {id_search}")
        print(f"Nombre del estudiante: {students[id_search]['full_name']}")
        print(f"Edad: {students[id_search]['age']}")
        print(f"Nota: {students[id_search]['note']}")
    else:
        print("\n\033[93m Estudiante no encontrado.\033[0m\n")

def update_information():
    print("-------------------- Actualizar estudiante --------------------")
    id_update = int(input("Ingrese el ID del estudiante que desea Actulizar: "))
    if id_update not in students:
        print("\n\033[93m El estudiante con el ID  no registado en el sistema.\033[0m\n")
    else:
        print("\n----- Actualice infomacion del estudiante.-----\n")
        new_age = int(input("Ingrese la edad del estudiante: "))
        new_note = float(input("Ingrese la nota del estudiante: "))

        students[id_update]["age"]= new_age
        students[id_update]["note"]= new_note
    
    print("\n\033[92mEstudiante con el ID {id_update} a sido actulizado correctamente\033[0m\n")

def delet_student():
    print("-------------------- Eliminar estudiante --------------------")
    id_delet = int(input("Ingrese el ID del estudiante que desea eliminar: "))
    if id_delet not in students:
        print("\n\033[93m El estudiante no se encuentra en el sistema.\033[0m\n")
    else:
        students.pop(id_delet)
        print(f"\n\033[92mEl estudiante con el ID {id_delet} fue eliminado con exito.\033[0m\n")

def calculate_average():
    print("-------------------- Promedio estudiantes --------------------")
    total_notes = 0.0
    counter = 0
    for student in students.values():
        counter += 1
        total_notes = total_notes + student["note"]
    
    average = total_notes / counter
    print("-------------------------------------------------------------------")
    print(f"\033[92mEl promedio de todos los estudiantes es {average}\033[0m")
    print("-------------------------------------------------------------------")

def low_redundancy():
    print("-------------------- Estudiantes con bajo rendimiento --------------------")
    for student in students.values():
        if student["note"] < 3.0:
        
            print(f"{student['full_name']} va perdiento con: {student['note']}")





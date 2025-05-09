from funciones import *

while True:
    print("""
    1) Agregar un estudiante
    2) Buscar estudiante pot ID.
    3) Actualizar informacion del estudiante.
    4) Eliminar estudiante.
    5) Calcular el promedio de notas.
    6) Listar estudiantes bajo rendimiento.
    7) Salir del sistema.
    """)

    opcion = int(input("Ingrese una OPCION: "))

    match opcion:
        case 1:
            main(aggregate_student)
        case 2:
            main(search_students)
        case 3:
            main(update_information)
        case 4:
            main(delet_student)
        case 5:
            main(calculate_average)
        case 6:
            main(low_redundancy)
        case 7:
            print("=======================================")
            print("Has salido del sistema... ¡Hasta luego!")
            print("=======================================")
            break
            
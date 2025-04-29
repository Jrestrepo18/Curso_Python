notas=[]


# 90 a 100: Excelente

# 80 a 89: Muy bueno

# 70 a 79: Bueno

# 60 a 69: Aprobado

# 0 a 59: Reprobado

# 1. Solicitar al usuario la calificación de un estudiante y almacenarla en una lista.
continuar = True
while continuar:
    calificacion = input(int("Ingrese la calificacion del estudiante: "))
    notas.append(calificacion)

    if calificacion <= 59:
        print("Reprobado")
    elif calificacion >= 60 and calificacion <= 69:
        print("Aprobado")
    elif calificacion >= 70 and calificacion <= 79:
        print("Bueno")
    elif calificacion >= 80 and calificacion <= 89:
        print("Muy bueno")
    else:
        print("Excelente")
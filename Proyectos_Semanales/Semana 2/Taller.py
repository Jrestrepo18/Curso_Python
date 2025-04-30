# Determinar el estado de aprobación:
# Solicitar al usuario ingresar una calificación numérica (de 0 a 100)
# Evaluar si el estudiante ha aprobado o reprobado basándose en la calificación

#90 a 100: Excelente
#80 a 89: Muy bueno
#70 a 79: Bueno
#60 a 69: Aprobado
#0 a 59: Reprobado

calificacion = float(input("Ingrese la calificacion del estudiante: "))
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


# 2. Calcular el promedio:
# Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
# Calcular y mostrar el promedio de las calificaciones en la lista.
notas=[]

calificaciones = input("Ingrese las calificaciones separadas por comas: ")
calificaciones = calificaciones.split(",")

notas_planas = [int(nota.strip()) for nota in calificaciones]

promedio = sum(notas_planas) / len(notas_planas)
print(f"El promedio es: {promedio:.2f}")


# 3. Contar calificaciones mayores:
# Preguntar al usuario por un valor específico
# Contar cuántas calificaciones en la lista son mayores que este valor

valor = int(input("Ingrese una nota (0 - 100) para comparar: "))

contador = 0
for nota in notas_planas:
    if nota > valor:
        contador += 1

print(f"Hay {contador} calificaciones mayores que {valor}.")
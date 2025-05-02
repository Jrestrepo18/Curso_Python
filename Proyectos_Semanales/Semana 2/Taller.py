# Determinar el estado de aprobación:
# Solicitar al usuario ingresar una calificación numérica (de 0 a 100)
# Evaluar si el estudiante ha aprobado o reprobado basándose en la calificación

#90 a 100: Excelente
#80 a 89: Muy bueno
#70 a 79: Bueno
#60 a 69: Aprobado
#0 a 59: Reprobado

RESET = '\033[0m'  
GREEN = '\033[32m'  
YELLOW = '\033[33m'  
BLUE = '\033[34m' 
RED = '\033[31m'  
MAGENTA = '\033[35m' 


calificacion = float(input("\nIngrese la calificación del estudiante: "))

if calificacion <= 59:
    print(f"{RED}Reprobado{RESET}")
elif calificacion >= 60 and calificacion <= 69:
    print(f"{YELLOW}Aprobado{RESET}")
elif calificacion >= 70 and calificacion <= 79:
    print(f"{BLUE}Bueno{RESET}")
elif calificacion >= 80 and calificacion <= 89:
    print(f"{MAGENTA}Muy bueno{RESET}")
else:
    print(f"{GREEN}Excelente{RESET}")

# 2. Calcular el promedio:
# Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
# Calcular y mostrar el promedio de las calificaciones en la lista.
notas_planas=[]

calificaciones = input("\nIngrese las calificaciones separadas por comas: ")
calificaciones = calificaciones.split(",")

notas_planas = [float(nota.strip()) for nota in calificaciones]

promedio = sum(notas_planas) / len(notas_planas)
print(f"El promedio es: {promedio:.2f}")


# 3. Contar calificaciones mayores:
# Preguntar al usuario por un valor específico
# Contar cuántas calificaciones en la lista son mayores que este valor

valor = float(input("\nIngrese una nota (0 - 100) para comparar: "))

contador = 0
for nota in notas_planas:
    if nota > valor:
        contador += 1

print(f"Hay {contador} calificaciones mayores que {valor}.")

# Verificar y contar calificaciones específicas
# Preguntar al usuario por una calificación específica. 
# Verificar si esta calificación está en la lista y contar cuántas veces aparece, utilizando break y continue para controlar el flujo del programa.


verificar=float(input("\nIngrese una calificacion: "))
c = 0

for i in notas_planas:
    if i != verificar:
        continue

    c += 1

if contador > 0:
    print(f"la calificacion {verificar} aparece en el contador {c} veces")
else:
    print(f"\n\033[31mLa calificación {verificar} no aparece en la lista\033[0m")





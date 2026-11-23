# Calcular el promedio de calificaciones de un grupo

alumnos = int(input("¿Cuántos alumnos hay en el grupo?: "))

suma = 0
aprobados = 0
reprobados = 0

if alumnos == 0:
    print("No hay calificaciones")

else:
    # Repite una vez por cada alumno para solicitar su calificación.
    for i in range(1, alumnos + 1):

        calificacion = float(input(f"Calificación del alumno {i}: "))

        suma = suma + calificacion

        if calificacion >= 6:
            aprobados = aprobados + 1
        else:
            reprobados = reprobados + 1

    promedio = suma / alumnos

    # Muestra los resultados.
    print(f"Suma de calificaciones: {suma}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Alumnos aprobados: {aprobados}")
    print(f"Alumnos reprobados: {reprobados}")
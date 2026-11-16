#Escamilla Balan Froy Adair
#Ejercicio 10. Examen de opción múltiple

aciertos = int(input("Ingresa la cantidad de aciertos: "))
errores = int(input("Ingresa la cantidad de errores: "))

if aciertos < 0 or errores < 0 or aciertos + errores > 20:
    print("Datos no validos")

else:
    calificacion = (aciertos * 0.5) - (errores * 0.25)

    print("Calificacion:", format(calificacion, ".2f"))

    if calificacion >= 6:
        print("Aprobo")
    else:
        print("Reprobo")
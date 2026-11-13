#Escamilla Froy
# Ejercicio 3: El año bisiesto

anio = int(input("Ingresa un año: "))

if anio % 4 == 0:
    if anio % 100 == 0:
        if anio % 400 == 0:
            print("El año", anio, "es bisiesto")
        else:
            print("El año", anio, "no es bisiesto")
    else:
        print("El año", anio, "es bisiesto")
else:
    print("El año", anio, "no es bisiesto")

#Escamilla Balan Froy Adair
#Ejercicio 3. Multa de la biblioteca
dias = int(input("Ingresa los dias de retraso: "))

if dias <= 0:
    print("No hay multa")
elif dias <= 3:
    multa = dias * 8
    print("Multa total: $", multa)
elif dias <= 7:
    multa = dias * 15
    print("Multa total: $", multa)
else:
    multa = dias * 25
    print("Multa total: $", multa)
    print("Suspension de 30 dias")

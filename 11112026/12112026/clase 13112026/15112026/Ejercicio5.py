#Escamilla Balan Froy Adair
#Ejercicio 5. El taxi

km = float(input("Ingresa los kilometros recorridos: "))
hora = int(input("Ingresa la hora del viaje (0 a 23): "))

if km > 0 and hora >= 0 and hora <= 23:

    total = 18 + (km * 9.50)

    if hora >= 22 or hora <= 5:
        total = total * 1.20

    print("Total a pagar: $", round(total, 2))

else:
    print("Datos no validos")
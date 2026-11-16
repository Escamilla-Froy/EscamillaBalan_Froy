#Escamilla Balan Froy Adair
#Ejercicio 4. Envío de un paquete

peso = float(input("Ingresa el peso del paquete en kg: "))
destino = int(input("Destino (1 = local, 2 = foraneo): "))

if peso > 0 and (destino == 1 or destino == 2):

    if peso <= 1:
        base = 60
    elif peso <= 5:
        base = 100
    else:
        base = 150

    if destino == 2:
        recargo = base * 0.25
    else:
        recargo = 0

    total = base + recargo

    print("Tarifa base: $", base)
    print("Recargo: $", recargo)
    print("Total a pagar: $", total)

else:
    print("Datos no validos")
#Escamilla Balan Froy Adair
#Ejercicio 9. Boleto de avión

clase = int(input("Clase (1 = economica, 2 = ejecutiva): "))
peso = float(input("Ingresa el peso del equipaje en kg: "))

if clase != 1 and clase != 2:
    print("Clase no valida")

else:
    if clase == 1:
        boleto = 1800
    else:
        boleto = 3200

    if peso <= 23:
        cargo = 0
    else:
        cargo = 600

    total = boleto + cargo

    print("Precio del boleto: $", boleto)
    print("Cargo por equipaje: $", cargo)
    print("Total a pagar: $", total)
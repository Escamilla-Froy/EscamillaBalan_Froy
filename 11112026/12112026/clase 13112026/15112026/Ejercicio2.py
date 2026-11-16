#Escamilla Balan Froy Adair
#Ejercicio 2. El recibo del agua

consumo = float(input("Ingresa los metros cubicos consumidos: "))

if consumo < 0:
    print("Consumo no valido")
elif consumo <= 10:
    total = 80
    print("Total a pagar: $", total)
elif consumo <= 20:
    total = 140
    print("Total a pagar: $", total)
elif consumo <= 30:
    total = 220
    print("Total a pagar: $", total)
else:
    total = 220 + (consumo - 30) * 12
    print("Total a pagar: $", total)
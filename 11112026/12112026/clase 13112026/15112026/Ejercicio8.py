#Escamilla Balan Froy Adair
#Ejercicio 8. Casa de cambio

cantidad = float(input("Ingresa la cantidad de pesos: "))
opcion = int(input("Moneda (1 = dolar, 2 = euro, 3 = dolar canadiense): "))

if cantidad <= 0:
    print("Cantidad no valida")

elif opcion < 1 or opcion > 3:
    print("Opcion no valida")

else:
    if opcion == 1:
        precio = 17.50
        print("Moneda: Dolar")
    elif opcion == 2:
        precio = 19.20
        print("Moneda: Euro")
    else:
        precio = 12.80
        print("Moneda: Dolar canadiense")

    unidades = cantidad / precio

    print("Puedes comprar:", round(unidades, 2))
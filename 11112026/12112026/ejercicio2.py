#Escamilla Froy
# Ejercicio 2: La pizzería

tamano = int(input("Ingresa el tamaño de la pizza (1, 2 o 3): "))
cantidad = int(input("¿Cuántas pizzas deseas?: "))

if tamano == 1:
    precio = 99
elif tamano == 2:
    precio = 149
elif tamano == 3:
    precio = 199
else:
    precio = 0
    print("Tamaño no válido")

if tamano >= 1 and tamano <= 3:
    if cantidad > 0:
        total = precio * cantidad

        if cantidad >= 3:
            total = total * 0.90

        print("Total a pagar: $", format(total, ".2f"))
    else:
        print("Cantidad no válida")
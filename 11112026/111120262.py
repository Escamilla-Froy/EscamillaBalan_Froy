# RETO EXPRESS
#Pide al usuario la longitud de tres lados. verifica si se puede formar un triangulo valido evaluando que la suma de cualquier par de lados sea mayor que el tercer lado. si el triangulo es valido, calcula el preimetro (Suma de todos los lados)


lado1 = float(input("Ingresa el lado 1: "))
lado2 = float(input("Ingresa el lado 2: "))
lado3 = float(input("Ingresa el lado 3: "))


if (lado1 > 0 and lado2 > 0 and lado3 > 0 and lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1):
    perimetro = lado1 + lado2 + lado3

    print("¡Se puede formar un triangulo!")
    print("El perimetro es:", perimetro )

else:
    print("No se puede formar un triangulo valido.")

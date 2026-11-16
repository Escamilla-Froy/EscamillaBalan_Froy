#Escamilla Balan Froy Adair
#Ejercicio 7. ¿Cuántas cifras tiene?

numero = int(input("Ingresa un numero entero: "))

if numero < 0:
    print("El numero debe ser positivo")
elif numero <= 9:
    print("Tiene 1 cifra")
elif numero <= 99:
    print("Tiene 2 cifras")
else:
    print("Tiene 3 cifras o mas")
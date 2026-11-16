#Escamilla Balan Froy Adair
#Ejercicio 6. Tres números en orden}

a = int(input("Ingresa el primer numero: "))
b = int(input("Ingresa el segundo numero: "))
c = int(input("Ingresa el tercer numero: "))

if a == b or a == c or b == c:
    print("Los numeros deben ser distintos")

elif a < b and a < c:
    if b < c:
        print(a, b, c, sep=", ")
    else:
        print(a, c, b, sep=", ")

elif b < a and b < c:
    if a < c:
        print(b, a, c, sep=", ")
    else:
        print(b, c, a, sep=", ")

else:
    if a < b:
        print(c, a, b, sep=", ")
    else:
        print(c, b, a, sep=", ")
#Ciclos en python
# Un ciclo es una estructura de control que permite ejecutar un bloque de código repetidamente mientras se cumpla una condición

#En python existen principalmente dos tipos de ciclos:
#1.-Ciclo "while" (mientras): Este ciclo se ejecuta mientras que una condición sea verdadera
#Sintaxis 
#While condicion
# bloque_de_codigo

#Ejemplo 1}
contador=0
while contador<10:
    print(contador)
    contador += 1 #El operador += incrementa el valor de la variable en 1
# Una de las recomendaciones a tomar con el ciclo while, es que debemos de contar con alguna variable que nos permita controla la condición del ciclo, para evitar que se ejecute indefinidamente

#Ejemplo 2.- Hacer un programa que solicite al usuario ingresar números hasta que ingrese un número negativo.
numero = int(input("Ingresa un número"))
while numero >= 0:
    numero = int(input("Ingresa un número: "))
print("Número negativo ingresado,programa terminado.")

#Ejemplo 3.- Hacer un programa que sume los números ingresados por el usuario hasta que se escriba un número negativo 
suma = 0
numero = int(input("Ingresa un número:"))
while numero >=0:
    suma += numero # A la variable suma,le iré sumando cada número ingresado en cada iteración
    numero = int(input("Ingresa un número: "))
print(f"Programa terminado... El resultado final de la suma es: {suma}")

#Ejemplo 4.- Haz un programa que solicite al usuario ingresar números hasta que escriba el numero 0. Cuenta la cantidad de números positivos y números negativos ingresados por el usuario y la suma total de todos los números ingresados.
positivos = 0
negativos = 0
suma = 0
numero = int(input("Ingresa un número: "))
while numero != 0:
    suma += número
    if numero > 0:
        postivos += 1
    else:
        negativos += 1
    numero = int(input("Ingresa un número: "))
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")
print(f"Suma total de todos los números ingresados: {suma}")
      
 # Ejercicio 5 .- Utilizando la libreria random () haz un programa que le pida al usuario ingresar un numero hasta adivinar el numero correcto.
 import random
 numero_correcto = random.randint(1, 100)
 numero_usuario = int(input ("Adivina el número entre 1 y 100: "))
 numero_intentos += 0
while (numero_usuario != numero_correcto) and (numero_intentos < 10):
    if numero_usuario < numero_correcto:
        print("Incorrecto, el número ingresado es menor que el número correcto.")
    else:
        print("Incorrecto, el número ingresado es mayor que el número correcto.")
    numero_usuario = int(input("Adivina el número entre 1 y 100: "))
    numero_intentos += 1
if numero_usuario == numero_correcto:
    print("¡Fedlicidades! Adivinaste el número correcto.")
    print(f"El número correcto era: {número_intentos}")
else:
    print("Lo siento, has alcanzado el número maximo de intentos.")
    print(f"El número correcto era: {numero_correcto}")
    


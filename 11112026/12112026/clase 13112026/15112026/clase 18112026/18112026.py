#Ciclo for: El ciclo for,tambien es un bucle al igual que el ciclo while,pero for se utiliza principalmente para iterar sobre una secuencia de elementos,como listas, tuplas, cadenas o rangos de numeros.

#Sintaxis basica del ciclo for
#for variable in secuencia
#bloque de codigo a ejecutar en cada iteracion
 
# Ciclo for en otros lenguajes de programación (Java):
# for (int i = 0; i < limite; i++) {
#Bloque de código a ejecutar en cada iteración
#}

#Ejemplo 1.- Haz un programa en python que imprima los numeros del 1 al 10 utilizando un ciclo for.
for i in range(1, 11):#Nota: i es una variable de control (variable bloque),que solo existe dentro dentro del ciclo for y no necesariamente tiene que llamarse i, ¿y porque range termina en 11 si quiero imprimir hasta el 10?  porque el segundo parametro de range es exclusivo,es decir, no se incluye en la secuencia generada.
    print(i)
    
    #Ejemplo 2.- Haz un programa que imprima los numeros pares del 1 al 100 
    for i in range(0, 101, 2): # Nota: El tercer parametro, indica el incremento o paso de la iteracion. Para este ejemplo, el paso es 2, es decir que aumentara de 2 en 2 en cada iteracion.
        print(i)
        
        #Ejemplo 3.- Haz un programa que imprima un conteo de los numeros del 100 al 0
        for i in range(100, -1, -1): 
            print(i)
#Ejemplo 4.- Haz un programa que solicite al usuario una palabra y que cuente cuantas vocales contiene (a, e, i, o ,u)
palabra = input("Ingrese una palabra: ")
vocales = "aeiou"
contado_vocales = 0
for letra in palabra:
    if letra in vocales: # in , verifica si un elemento esta presente en una secuencia (lista,tupla cadena, etc.) En este ejemplo, verifica si la letra actual, está  en la cadena vocales.
        contado_vocales += 1
    if letra.lower() == "a" or letra.lower() == "e" or letra.lower() == "i" or letra.lower() == "o" or letra.lower() == "u":
        contado_vocales += 1
print(f"La palabra '{palabra}' contiene {contado_vocales} vocales.")

#Ejemplo 5.- Hacer un programa que solicite al usuario un número y que imprima la suma de todos los números del 1 hasta ese número
numero = int(input("Ingrese un número: "))
suma = 0
for i in range(1, numero + 1):
    suma += i
print(f"La suma de los números del 1 al {numero} es: {suma}")

#RETO

#Ejemplo 6.- Haz un programa que solicite al usuario un número y que imprima la tabla de multiplicar de ese número del 1 al 10
numero = int(input("Ingrese un número: "))
multiplicacion = 0
for i in range(1, 11):
    multiplicacion = numero * i
    print(f"{numero} x {i} = {multiplicacion}") 
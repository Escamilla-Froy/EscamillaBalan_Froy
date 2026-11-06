# Ejercicio 1 Diseña un programa que reciba una cantidad total de dulces y un número de niños. Debe calcular cuántos dulces le tocan a cada uno de forma equitativa y cuántos dulces sobran en la caja.

dulces = int(input("Cantidad total de dulces: "))
ninos = int(input("Número de niños: "))
# Dulces por niño (división entera)
dulces_por_nino = dulces // ninos
# Dulces que sobran (residuo)
dulces_sobrantes = dulces % ninos
print("Dulces por niño:", dulces_por_nino)
print("Dulces sobrantes:", dulces_sobrantes)

# Ejercicio 2 Haz un programa que reciba la velocidad de un automóvil y determine de forma booleana (True o False) si ha excedido el límite permitido de 90 km/h

velocidad = float(input("Velocidad del automóvil (km/h): "))
excedio_limite = velocidad > 90  # True si excedió, False si no
print(excedio_limite)

# Ejercicio 3 Crea un programa que convierta una temperatura dada en grados Celsius a grados Fahrenheit. Muestra en pantalla el resultado de la conversión.

celsius = float(input("Temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperatura en grados Fahrenheit: ", fahrenheit)

# Ejercicio 4 
lado1 = float(input("Longitud del lado 1: "))
lado2 = float(input("Longitud del lado 2: "))
lado3 = float(input("Longitud del lado 3: "))
# Verificación de triángulo: suma de cada par > tercer lado
es_triangulo = (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1)
print(es_triangulo)

# Ejercicio 5 Solicita un número entero y determina si es un múltiplo simultaneo de 3 y de 5 (Es decir, que al dividirlo entre ambos el residuo sea cero)

numero = int(input("Número entero: "))
multiplo_3 = (numero % 3 == 0)
multiplo


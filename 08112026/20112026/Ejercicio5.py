# Mostrar una palabra al revés y contar sus letras

palabra = input("Ingresa una palabra: ")

contador = 0
contador_a = 0
invertida = ""

# Recorre cada letra de la palabra.
for letra in palabra:

    print(letra)

    contador = contador + 1

    if letra == "a":
        contador_a = contador_a + 1

    # Agrega cada letra al inicio para invertir la palabra.
    invertida = letra + invertida

# Muestra los resultados.
print(f"Cantidad de letras: {contador}")
print(f"Palabra invertida: {invertida}")
print(f"La letra a aparece: {contador_a} veces")
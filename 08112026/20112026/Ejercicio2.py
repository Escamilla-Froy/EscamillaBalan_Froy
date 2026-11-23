# Suma de números pares e impares del 1 al 100

suma_pares = 0
suma_impares = 0
contador_pares = 0
contador_impares = 0

# Recorre los números del 1 al 100.
for numero in range(1, 101):

    if numero % 2 == 0:
        suma_pares = suma_pares + numero
        contador_pares = contador_pares + 1
    else:
        suma_impares = suma_impares + numero
        contador_impares = contador_impares + 1

# Muestra los resultados.
print(f"Suma de pares: {suma_pares}")
print(f"Suma de impares: {suma_impares}")
print(f"Cantidad de pares: {contador_pares}")
print(f"Cantidad de impares: {contador_impares}")
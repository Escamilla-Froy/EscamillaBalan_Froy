#Escamilla Froy
# Ejercicio 4: Piedra, papel o tijera

jugador1 = input("Jugador 1, escribe piedra, papel o tijera: ")
jugador2 = input("Jugador 2, escribe piedra, papel o tijera: ")

jugador1 = jugador1.lower()
jugador2 = jugador2.lower()

if (jugador1 != "piedra" and jugador1 != "papel" and jugador1 != "tijera") or (jugador2 != "piedra" and jugador2 != "papel" and jugador2 != "tijera"):
    resultado = "Jugada no válida"

elif jugador1 == jugador2:
    resultado = "Empate"

elif jugador1 == "piedra":
    if jugador2 == "tijera":
        resultado = "Gana el jugador 1"
    else:
        resultado = "Gana el jugador 2"

elif jugador1 == "papel":
    if jugador2 == "piedra":
        resultado = "Gana el jugador 1"
    else:
        resultado = "Gana el jugador 2"

else:
    if jugador2 == "papel":
        resultado = "Gana el jugador 1"
    else:
        resultado = "Gana el jugador 2"

print(resultado)
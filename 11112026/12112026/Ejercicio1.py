#Escamilla Froy
# Ejercicio 1: El semáforo

color = input("Ingresa el color del semáforo: ")
color = color.lower()

if color == "rojo":
    print("Alto total")
elif color == "amarillo":
    print("Precaución, disminuye la velocidad")
elif color == "verde":
    print("Puedes avanzar")
else:
    print("Color no válido")
# Control de acceso a la caja fuerte

contrasena_correcta = "python2026"
intentos = 0
acceso = False

# Repite mientras la contraseña sea incorrecta
# y todavía queden intentos disponibles.
while intentos < 3 and acceso == False:
    contrasena = input("Ingresa la contraseña: ")
    intentos = intentos + 1

    if contrasena == contrasena_correcta:
        acceso = True
    else:
        print("Contraseña incorrecta")

# Muestra el resultado del acceso.
if acceso == True:
    print("Acceso concedido")
else:
    print("Cuenta bloqueada")

print(f"Intentos realizados: {intentos}")
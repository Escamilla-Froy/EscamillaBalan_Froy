# Simulación de un cajero automático

saldo = 5000.00
opcion = 0

# Repite el menú hasta que el usuario seleccione la opción 3.
while opcion != 3:

    print("\n--- CAJERO AUTOMÁTICO ---")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Salir")

    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        print(f"Tu saldo actual es: ${saldo:.2f}")

    elif opcion == 2:
        monto = float(input("¿Cuánto deseas retirar?: "))

        if monto <= 0:
            print("El monto debe ser mayor que cero")

        elif monto > saldo:
            print("Fondos insuficientes")

        else:
            saldo = saldo - monto
            print("Retiro exitoso")
            print(f"Saldo restante: ${saldo:.2f}")

    elif opcion == 3:
        print("Gracias por utilizar el cajero")

    else:
        print("Opción no válida")
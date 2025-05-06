saldo = 0
historial = []
usurios = {}
while True:
    print("1. Ver el saldo de la cuenta.")
    print("2. Retirar dinero.")
    print("3. Depositar dinero.")
    print("4. Ver historial de movimientos.")
    print("5. salir.")

    op = int(input("\n Ingrese una opcion: "))

    if op == 1:
        print(f"\nSu saldo es: {saldo}")
    elif op == 2:
        print(f"Su saldo actual es {saldo}")
        retirar = float(input("\nDigite el monto a retirar: "))
        saldo -= retirar
        historial.append (f"-{retirar}",)
        print(f"Su retiro a sido exitoso.")
    elif op == 3:
        deposito = float(input("Digite el monto a depositas: "))
        saldo += deposito
        historial.append((f"+{deposito}",))
        print("Consignado.")
    elif op == 4:
        print("Movimientos: ")
        for mov in historial:
            print(mov)
    elif op == 5:
        print("Has salido del sistema.")
        break

    continuar = int(input("\n¿Deseas continuar? 1.Si - 2.No "))
    if continuar != 1:
        break


       
      
        
    
       
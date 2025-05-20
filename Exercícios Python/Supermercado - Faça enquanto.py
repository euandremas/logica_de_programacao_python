proximoCliente = "S"

while proximoCliente == "S":
    # Solicita o valor das compras
    while True: 
        valorDasCompras = float(input("Digite o valor das compras: R$ "))
        if valorDasCompras > 0:
            break

    # Solicita o pagamento e garante que seja suficiente
    while True:
        pgtoCliente = float(input("Digite o valor pago pelo cliente: R$ "))
        if pgtoCliente >= valorDasCompras:
            break
        else:
            print("❌ O valor em dinheiro não é suficiente para pagar as compras. Tente novamente.")

    troco = pgtoCliente - valorDasCompras
    print(f"✅ Troco: R$ {troco:.2f}")
    print("Volte sempre!\n")

    proximoCliente = input("Deseja atender outro cliente? (S/N): ").strip().upper()








































quantidadeAcai = int(input("Digite a quantidade de açaí: "))  
quantidadeTapioca = int(input("Digite a quantidade de tapioca: "))    
valorAcai = 12.00
valorTapioca = 15.00
valorTotal = (quantidadeAcai * valorAcai) + (quantidadeTapioca * valorTapioca)
if valorTotal >= 100:
    formadePgto = str(input("Digite D para pagamento em dinheiro, P para pagamento em PIX e O para outras formas de pagamento: "))
    if formadePgto == "D" or formadePgto == "P":
        print ("Valor era de: R$", valorTotal, ", mas com o desconto de 10%, seu pedido saiu por: R$", valorTotal*0.9)
    else:
        print   ("Valor era de: R$", valorTotal, ", mas com o desconto de 5%, seu pedido saiu por: R$", valorTotal*0.95)

        print ("Muito obrigado, volte sempre!!!")
else:
        print ("Valor total sem desconto: R$", valorTotal)
        print ("Muito obrigado, volte sempre!!!")
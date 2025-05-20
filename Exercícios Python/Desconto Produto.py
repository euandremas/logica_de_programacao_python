valorProduto = float(input("Digite o valor do produto: "))
if valorProduto <=  100:
    print("Não tem desconto")
elif valorProduto <= 250:
    print("Desconto de 10%")
elif valorProduto <= 500:
    print("Desconto de 20%")
else:
    print("Desconto de 30%")
# Fim do programa
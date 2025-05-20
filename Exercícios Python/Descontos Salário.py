salarioBruto = float(input("Digite seu salário bruto: "))
previdencia = 0.12
valeTransporte = 0.06
calculoDescontos = (salarioBruto * previdencia) + (salarioBruto * valeTransporte)
descontoTotal = calculoDescontos
salarioLiquido = salarioBruto - descontoTotal
print("O total de descontos no seu salário é de: R$", round(descontoTotal,2), " e o valor líquido que você irá receber é de: R$", round(salarioLiquido,2))

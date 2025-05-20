numero = int(input("Digite um número inteiro N: "))

if numero < 0:
    print("Por favor, insira um número inteiro não negativo.")
else:
    soma = 0
    for i in range(1, numero + 1):  
        soma += i  

    print(f"A soma dos primeiros {numero} números naturais é: {soma}")

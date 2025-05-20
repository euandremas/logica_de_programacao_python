numero = int(input("Digite um número inteiro para calcular seu fatorial: "))

if numero < 0:
    print("Não é possível calcular o fatorial de um número negativo.")
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    print(f"O fatorial de {numero} é {fatorial}")


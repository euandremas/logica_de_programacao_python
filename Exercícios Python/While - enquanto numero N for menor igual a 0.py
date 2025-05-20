numeroN = int(input("Digite um número: "))
qtd = 1
while numeroN > 0:
    numeroN = int(input("Digite outro número: "))
    qtd += 1
print("A quantidade de números digitados foi:", qtd, "números.")

# O código acima conta quantos números foram digitados pelo usuário, enquanto o número for maior que 0.
# O loop continua até que o usuário digite um número menor ou igual a 0.
# O código imprime a quantidade de números digitados.
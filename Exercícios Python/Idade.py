nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
print(f"Olá {nome}! Constatamos que você tem {idade} anos. Isso é muito legal!")
print("Você é um jovem adulto!" if idade < 30 else "Você é um adulto!")

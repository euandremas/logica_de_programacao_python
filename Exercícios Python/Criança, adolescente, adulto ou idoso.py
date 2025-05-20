idade = int(input("Por favor, insira sua idade: "))
        
if idade < 0:
            print("Idade inválida. Por favor, insira um número positivo.")
elif idade <= 12:
            print("Você é classificado como: Criança.")
elif idade <= 17:
            print("Você é classificado como: Adolescente.")
elif idade <= 64:
            print("Você é classificado como: Adulto.")
else:
            print("Você é classificado como: Idoso.")
    
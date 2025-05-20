nome1 = input("Digite o nome do primeiro usuário: ")

idade1 = int(input(f"Digite a idade de {nome1}: "))

 

 

nome2 = input("Digite o nome do segundo usuário: ")

idade2 = int(input(f"Digite a idade de {nome2}: "))

 

if idade1 > idade2:

  print(f"{nome1} é mais velho.")

 

elif idade1 < idade2:

  print(f"{nome2} é mais velho.")

 

else:

  print("Ambos têm a mesma idade.")
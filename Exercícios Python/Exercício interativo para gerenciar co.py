# Exercício interativo para gerenciar contatos
print("Bem-Vinda ao Gerenciador de Contatos")

while True:
    print("\n=== Menu ===")
    print("1. Adicionar contato")
    print("2. Remover contato")
    print("3. Exibir todos os contatos")
    print("4. Buscar número de telefone por nome")
    print("5. Sair")

    escolha = input("Escolha uma opção (1-5): ")

    if escolha == "1":
        print("\n=== Adicionar Contato ===")
        nome = input("Digite o nome do novo contato: ")
        telefone = input("Digite o número de telefone: ")
        contatos[nome] = telefone
        print(f"Contato '{nome}' adicionado com sucesso.")
    elif escolha == "2":
        print("\n=== Remover Contato ===")
        nome = input("Digite o nome do contato a ser removido: ")
        if nome in contatos:
            del contatos[nome]
            print(f"Contato '{nome}' removido com sucesso.")
        else:
            print(f"Contato '{nome}' não encontrado.")
    elif escolha == "3":
        print("\n=== Exibir Todos os Contatos ===")
        for nome, telefone in contatos.items():
            print(f"{nome}: {telefone}")
    elif escolha == "4":
        print("\n=== Buscar Número de Telefone por Nome ===")
        nome = input("Digite o nome do contato: ")
        if nome in contatos:
            print(f"Número de telefone de '{nome}': {contatos[nome]}")
        else:
            print(f"Contato '{nome}' não encontrado.")
    elif escolha == "5":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
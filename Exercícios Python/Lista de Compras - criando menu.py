#Lista de Compras

Lista = []

# Exibe um menu com 3 opções
def menu():
    print("\n=== Lista de Compras ===")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Listar itens")
    print("4 - Sair")

    while True: # Loop infinito até que uma opção válida seja escolhida
        try:
            opcao_str = input("Escolha uma opção: ")
            opcao = int(opcao_str)

            # Verifica se a opção está entre 1 e 4
            if 1 <= opcao <= 4:
                return opcao # Retorna a opção válida e sai do loop
            else:
                print("Opção inválida. Por favor, digite um número entre 1 e 4.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
#continuar o loop enquanto a opção for diferente de 4
while True:
    opcao = menu()
    # Adiciona um item à lista
    if opcao == 1:
        item = input("Digite o nome do item: ")
        Lista.append(item)
        print(f"{item} adicionado à lista.")
    # Remove um item da lista
    elif opcao == 2:
        item = input("Digite o nome do item a ser removido: ")
        if item in Lista:
            Lista.remove(item)
            print(f"{item} removido da lista.")
        else:
            print(f"{item} não encontrado na lista.")
    # Lista os itens
    elif opcao == 3:
        print("Lista de Compras:")
        if Lista:
            for exibir, item in enumerate(Lista, start=1):
                print(f"{exibir}. {item}")
        else:
            print("Lista vazia.")
        
    # Sai do loop
    elif opcao == 4:
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
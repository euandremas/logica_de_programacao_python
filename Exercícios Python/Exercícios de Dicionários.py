# # Exercícios de Dicionários
dicionario_vazio = {}

# # Dicionário com pares chave-valor
# pessoa = {
#     "nome": "Lucas",
#     "idade": 20,
#     "altura": 1.75,
#     "profissao": "Estudante",
#     "cidade": "São Paulo"
# }

#Dicionários aninhados

# empresa = {
#     "nome": "Tech Solutions",
#     "endereco": {
#         "rua": "Avenida Paulista",
#         "numero": 1000,
#         "bairro": "Centro",
#         "cidade": "São Paulo",
#         "estado": "SP"
#     },
#     "funcionarios": [
#         {
#             "nome": "Ana",
#             "cargo": "Desenvolvedora",
#             "salario": 5000
#         }
#     ]
# }

# # Acessando valor em um dicionário aninhado
# print(empresa["funcionarios"][0]["nome"])  # Imprime "Ana"



# # Verificar exsistência de uma chave no dicionário
# if "nome" in pessoa:
#     print("A chave 'nome' existe no dicionário.")

# # Exemplo de uso de dicionário

# print(pessoa.keys())  # Imprime as chaves do dicionário
# print(pessoa.values())  # Imprime os valores do dicionário
# print(pessoa.items())  # Imprime os pares chave-valor do dicionário



#Iterando pelas chaves do dicionário

# for chave in pessoa:
#     print(chave)#.keys() # Posso usar o método keys() para obter as chaves ou não que da no mesmo

# # Iterando pelos valores do dicionário
# for valor in pessoa.values():
#     print(valor)

# # Iterando pelos pares chave-valor do dicionário
# for chave, valor in pessoa.items():
#     print(f"{chave}: {valor}")


# print(pessoa)

# # Acessando valores

# print(pessoa["nome"])  # Acessando o valor da chave "nome"
# print(pessoa["idade"])  # Acessando o valor da chave "idade"

# # Adicionando/Alterando novos pares chave-valor
# pessoa['profissao'] = 'Engenheiro'

# # Atualizando o valor de uma chave existente
# pessoa['idade'] = 21
# print(pessoa)

# # # # # Removendo pares chave-valor sem salvar o valor

# del pessoa['cidade']  # Deletando a chave "cidade" sem salvar o valor

# # Método pop() para remover e retornar o valor de uma chave
# profissao_removida = pessoa.pop('profissao')  # Deletando a chave "profissao" e salvando o valor

# print(pessoa)
# print(profissao_removida)  # Imprimindo o valor removido

# # # del pessoa['altura']  # Deletando a chave "altura" sem salvar o valor
# # # print(pessoa)

# # # # # Removendo pares chave-valor e salvando o valor
# # altura = pessoa.pop('altura')  # Deletando a chave "altura" e salvando o valor
# # print(pessoa)


# Dicionário inicial de contatos (nome: número de telefone)
contatos = {
    "Lucas": "1234-5678",
    "Ana": "9876-5432",
    "Carlos": "5555-5555"
}

# Dicionário inicial de contatos (nome: número de telefone)
contatos = {
    "Lucas": "1234-5678",
    "Ana": "9876-5432",
    "Carlos": "5555-5555"
}

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

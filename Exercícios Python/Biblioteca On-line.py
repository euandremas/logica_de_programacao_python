# Biblioteca On-line

biblioteca = {
    'livros': {
        'Pai Rico, Pai Pobre': {
            'autor': 'Robert Kiyosaki',
            'ano': 1997,
            'disponivel': True
        },
        'O Poder do Hábito': {
            'autor': 'Charles Duhigg',
            'ano': 2012,
            'disponivel': True
        },
        'Os Segredos da Mente Milionária': {
            'autor': 'T. Harv Eker',
            'ano': 2005,
            'disponivel': False
        },
        'Seja Foda!': {
            'autor': 'Jéfferson L. de Andrade',
            'ano': 2018,
            'disponivel': True
        },
        'O Homem Mais Rico da Babilônia': {
            'autor': 'George S. Clason',
            'ano': 1926,
            'disponivel': True
        },
        'Deixe de Ser Pobre': {
            'autor': 'Eduardo Feldberg',
            'ano': 2024,
            'disponivel': True
        },
        'Quem Pensa Enriquece': {
            'autor': 'Napoleon Hill',
            'ano': 1937,
            'disponivel': True
        },
        'Casais Inteligentes Crescem Juntos':{
            'autor': 'Gustavo Cerbasi',
            'ano': 2004,
            'disponivel': True
        },
                'Trabalhe 4 Horas por Semana':{
                    'autor': 'Tim Ferriss',
                    'ano': 2007,
                    'disponivel': True
                }
            }
        }
while True:
    print("\n=== Menu ===")
    print("1. Adicionar livro")
    print("2. Remover livro")
    print("3. Exibir títulos dos livros")
    print("4. Exibir detalhes de um livro")
    print("5. Sair")
    escolha = input("Escolha uma opção (1-5): ")

    if escolha == "1":
        print("\n=== Adicionar Livro ===")
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano = int(input("Digite o ano de publicação: "))
        disponivel = input("O livro está disponível? (s/n): ").lower() == 's'
        biblioteca['livros'][titulo] = {
            'autor': autor,
            'ano': ano,
            'disponivel': disponivel
        }
        print(f"Livro '{titulo}' adicionado com sucesso.")
    elif escolha == "2":
        print("\n=== Remover Livro ===")
        titulo = input("Digite o título do livro a ser removido: ")
        if titulo in biblioteca['livros']:
            del biblioteca['livros'][titulo]
            print(f"Livro '{titulo}' removido com sucesso.")
        else:
            print(f"Livro '{titulo}' não encontrado.")
    elif escolha == "3":
        print("\n=== Exibir Títulos dos Livros ===")
        for titulo in biblioteca['livros']:
            print(titulo)
    elif escolha == "4":
        print("\n=== Exibir Detalhes de um Livro ===")
        titulo = input("Digite o título do livro: ")
        if titulo in biblioteca['livros']:
            livro = biblioteca['livros'][titulo]
            print(f"Título: {titulo}")
            print(f"Autor: {livro['autor']}")
            print(f"Ano: {livro['ano']}")
            print(f"Disponível: {'Sim' if livro['disponivel'] else 'Não'}")
        else:
            print(f"Livro '{titulo}' não encontrado.")
    elif escolha == "5":
        print("Saindo do programa...")
        break
            

  
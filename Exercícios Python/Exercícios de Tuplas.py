#Tuplas

# # Tuplas são estruturas de dados semelhantes a listas, mas imutáveis.

# # Isso significa que, uma vez criadas, não podem ser alteradas. Elas são úteis para armazenar dados que não precisam ser modificados.


# tupla1 = (1, 2, 3, 4, 5)
# tupla2 = ('a', 'b', 'c', 'd', 'e')
# tupla3 = (1, 'dois', 3.0, [4, 5])
# tupla4 = tupla1 + tupla2  # Concatenando tuplas
# tupla5 = tupla1 * 2  # Repetindo tupla
# tupla6 = (1, 2, 3, 4, 5, 1, 2 , 3, 5 , 1)  # Tupla com elementos repetidos

# # # Exibindo resultados
# print(tupla6.count(1))  # Contando quantas vezes o número 1 aparece na tupla
# print(tupla2.index('b'))  # Encontrando o índice do primeiro elemento 3

# tupla_original = (1, 2, 3, 4, 5)
# lista_temporaria = list(tupla_original)  # Convertendo tupla para lista
# # Adicionando elemento à lista
# lista_temporaria.append(6)
# lista_temporaria.append(7)
# # Convertendo lista de volta para tupla
# tupla_modificada = tuple(lista_temporaria)
# # Exibindo resultados
# print("Tupla original:", tupla_original)
# print("Tupla modificada:", tupla_modificada)

# # Acessando elementos
# print(tupla1[0])  # 1
# print(tupla2[1])  # 'b'
# print(tupla3[2])  # 3.0
# print(tupla4)  # (1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e')
# print(tupla5)  # (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

#iterando atraves dos elementos da tupla

# for elemento in tupla1:
#     print(elemento)  # 1, 2, 3, 4, 5

# # Desempacotando tuplas
# a, b, c, d, e = tupla2
# print(a)  # 'a'
# print(b)  # 'b'   
# print(c)  # 'c'
# print(d)  # 'd'
# print(e)  # 'e'

# n1, n2, n3, n4, n5 = tupla1
# print(n1, n2 , n3)  # Saída: 1 2 3

# #Média de notas

# tupla_dados_aluno = ('Lucas', 'Silva', 20, 1.75, 'Estudante')
# tupla_nota_portugues = (8.5, 9.0, 7.5)
# tupla_nota_matematica = (9.0, 8.5, 10.0)
# tupla_nota_artes = (7.0, 8.0, 9.5)
# tupla_nota_inglês = (8.0, 9.5, 7.5)

# # # Desempacotando a tupla
# nome, sobrenome, idade, altura, ocupacao = tupla_dados_aluno
# print("Nome:", nome)
# print("Sobrenome:", sobrenome)
# print("Idade:", idade)
# print("Altura:", altura)
# print("Ocupação:", ocupacao)
# # # Exibindo notas
# print("Notas de Português:", tupla_nota_portugues)
# print("Notas de Matemática:", tupla_nota_matematica)
# print("Notas de Artes:", tupla_nota_artes)
# print("Notas de Inglês:", tupla_nota_inglês)
# # # Exibindo média das notas de cada disciplina
# todas_as_notas = tupla_nota_portugues + tupla_nota_matematica + tupla_nota_artes + tupla_nota_inglês
# mediaParaAprovacao = sum(todas_as_notas) / len(todas_as_notas)

# # # Exibindo média das notas
# print("Média para aprovação:", mediaParaAprovacao)
# print("Aprovado?" , mediaParaAprovacao >= 6.0)

# # Exemplo 2

aluno = ("André", 9.1, 8.5, 7.0, 6.5, 8.0)

nome, notaPortugues, notaMatematica, notaCiencias, notaArtes, notaIngles = aluno

print(f"Notas do aluno {nome}:")
print(f"Português: {notaPortugues}")
print(f"Matemática: {notaMatematica}")
print(f"Ciências: {notaCiencias}")
print(f"Artes: {notaArtes}")
print(f"Inglês: {notaIngles}")

# Calculando a média das notas
media = (notaPortugues + notaMatematica + notaCiencias + notaArtes + notaIngles) / 5
print(f"Média: {media:.2f}")
# Verificando se o aluno foi aprovado
if media >= 6.0:
    print("Aprovado!")
else:
    print("Reprovado!")
#fim 







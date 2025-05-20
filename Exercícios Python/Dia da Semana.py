diaSemana = int(input("Digite o dia da semana : "))
if diaSemana == 1:
    print("Domingo")
elif diaSemana == 2:
    print("Segunda-feira")
elif diaSemana == 3:
    print("Terça-feira")
elif diaSemana == 4:
    print("Quarta-feira")
elif diaSemana == 5:
    print("Quinta-feira")
elif diaSemana == 6:
    print("Sexta-feira")
elif diaSemana == 7:
    print("Sábado")
else:
    print("Dia da semana inválido - digite um número de 1 a 7!")
# fim do programa

# Este programa lê um número inteiro de 1 a 7 e imprime o dia da semana correspondente.
# O programa utiliza uma série de instruções condicionais (if, elif, else) para verificar o valor
# do número e imprimir o dia da semana correspondente. Se o número não estiver entre 1 e 7, o programa
# imprime "Número inválido".
# O programa é simples e fácil de entender, e pode ser útil para quem precisa lembrar os dias da semana
# ou para quem está aprendendo a programar em Python.
# O código pode ser melhorado utilizando um dicionário para mapear os números aos dias da semana,
# tornando-o mais conciso e fácil de manter.
# Exemplo de melhoria:

# dias_da_semana = {
#     1: "Domingo",
#     2: "Segunda-feira",
#     3: "Terça-feira",
#     4: "Quarta-feira",
#     5: "Quinta-feira",
#     6: "Sexta-feira",
#     7: "Sábado"
# }
# diaSemana = int(input("Digite o dia da semana : "))
# print(dias_da_semana.get(diaSemana, "Número inválido"))

# O dicionário 'dias_da_semana' mapeia os números de 1 a 7 para os dias da semana correspondentes.
# O método 'get' do dicionário retorna o valor correspondente à chave 'diaSemana', ou "Número inválido"
# se a chave não existir no dicionário. Isso torna o código mais limpo e fácil de entender.
# Além disso, o uso de dicionários é uma prática comum em Python e pode ser mais eficiente
# em termos de desempenho, especialmente quando há muitas opções a serem verificadas.

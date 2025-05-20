# numeroAlunos = int(input("Digite o número de alunos: "))
# somaNotas = 0
# for i in range(1, numeroAlunos  + 1):
#     nota = float(input("Digite a nota do aluno %d: " % i))
#     somaNotas += nota
# media = somaNotas / numeroAlunos
# print("A média das notas é: %.2f" % media)

numeroAlunos = int(input("Digite o número de alunos: "))
somaNotas = 0

for i in range(1, numeroAlunos + 1):
    while True:
        try:
            nota = float(input("Digite a nota do aluno %d (0 a 10): " % i))
            if 0 <= nota <= 10:
                break
            else:
                print("⚠️ A nota deve estar entre 0 e 10. Tente novamente.")
        except ValueError:
            print("❌ Entrada inválida! Digite um número válido.")

    somaNotas += nota

media = somaNotas / numeroAlunos
print("A média das notas é: %.2f" % media)

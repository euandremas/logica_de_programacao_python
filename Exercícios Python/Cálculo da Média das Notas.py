soma_notas = 0
quantidade_notas = 0

while True:
    nota = float(input("Insira uma nota (0 a 10): "))
    
    if 0 <= nota <= 10:
        soma_notas += nota
        quantidade_notas += 1
    else:
        print("Nota inválida. Digite um valor entre 0 e 10.")
        continue  # volta pro início do laço

    continuar = input("Deseja inserir outra nota? (S/N): ").strip().upper()
    if continuar != "S":
        break

if quantidade_notas > 0:
    media = soma_notas / quantidade_notas
    print(f"\nA média das notas inseridas é: {media:.2f}")
else:
    print("Nenhuma nota válida foi inserida.")
# Fim do código
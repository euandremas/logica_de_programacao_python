# Gera uma lista de 10 números aleatórios entre 1 e 100
import random
tamanho_lista = random.randint(5, 20)
numeros_aleatorios = [random.randint(1, 100) for i in range(tamanho_lista)]

# numeros_aleatorios = []
# for elemento in range(tamanho_lista):
#     numeros_aleatorios.append(random.randint(1, 100))

# Solicita ao usuário um palpite
palpite = int(input("Tente adivinhar um número entre 1 e 100: "))

# Verifica se o palpite está na lista
acertou = palpite in numeros_aleatorios

# Exibe os resultados
print(f"\nLista de números gerados: {numeros_aleatorios}")
print("Você acertou!" if acertou else "Você errou!")
print("Maior número gerado:", max(numeros_aleatorios))
print("Menor número gerado:", min(numeros_aleatorios))
print("Média dos números gerados:", sum(numeros_aleatorios) / len(numeros_aleatorios))

import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Início do programa
limpar_tela()
print("=== Calculadora de Hidratação ===")
nome = input("Digite seu nome: ")

limpar_tela()
print(f"Olá, {nome}!")
idade = int(input("Digite sua idade: "))

limpar_tela()
print(f"{nome}, {idade} anos... Tá jovem ainda! 😄")
peso = float(input("Digite seu peso (em kg): "))

# Cálculo da água necessária
agua_por_ml = peso * 35
agua_por_l = agua_por_ml / 1000

limpar_tela()
print(f"{nome}, com {peso}kg, você deve beber aproximadamente {round(agua_por_l, 2)} litros de água por dia.")
print("\nDica: beba aos poucos durante o dia e mantenha-se hidratado! 💧")

# Espera antes de finalizar
time.sleep(10)
limpar_tela()
print("Programa finalizado. Até a próxima! 👋")

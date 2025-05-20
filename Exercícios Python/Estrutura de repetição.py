import os
import time

def limpar_tela():
    """Função para limpar a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

# Loop para contar até 10
for i in range(10):
    print(i+1)  # Mostra o número
    time.sleep(0)  # Espera por 0 segundo entre os números


time.sleep(2)  # Espera 2 segundos antes de limpar a tela


limpar_tela()# Limpa a tela após 2 segundos

print("Contagem finalizada!")

time.sleep(2) # Espera 2 segundos antes de limpar a tela

limpar_tela() # Limpa a tela após 2 segundos

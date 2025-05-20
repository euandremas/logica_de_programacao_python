letra = str(input("Digite uma letra: ")).strip().lower()
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("A letra digitada é uma vogal.")  
elif letra.isalpha() and letra not in "aeiou":
    print("A letra digitada é uma consoante.")
else:
    print("Não é uma letra.")
    # Fim do programa
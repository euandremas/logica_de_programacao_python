notaPortugues = float(input("Digite a nota de português: "))
notaMatematica = float(input("Digite a nota de matemática: "))
if notaPortugues >= 6:
    if notaMatematica >= 6:
        print("Aprovado em ambas as disciplinas")
    else:
        print("Reprovado em matemática")
else:
    if notaMatematica >= 6:
        print("Reprovado em português")
    else:
        print("Reprovado em ambas as disciplinas")
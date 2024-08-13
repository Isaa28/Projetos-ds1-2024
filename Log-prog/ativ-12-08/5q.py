nome = input("Digite seu nome: ")
disciplina = input("Digite a disciplina: ")
nota = float(input("Digite sua nota: "))
if nota < 0 or nota > 10:
    print("Nota inválida. Tente novamente.")
else:
    if nota > 5.5 and nota < 6:
        nota = 6
    if nota >= 6:
        status = "aprovado(a)"
    else:
        status = "reprovado(a)"
    print(f"{nome} está {status} em {disciplina} com nota {nota}.")
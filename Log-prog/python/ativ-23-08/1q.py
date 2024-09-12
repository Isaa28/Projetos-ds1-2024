op = " "
while op == " " :
    print(""" 
    -----------Calc.py----------
    Escolha uma operação:
    1-Soma
    2-Subtração
    3-Multiplicação
    4-Divisão
    5-Elevado ao quadrado
    0-sair
    """)
    op = input("Digite sua operação: ")
    if op not in ["1" , "2" , "3" , "4" , "5" , "0"]:
        print("Operação inválida, tente novamente.")
        op = " "
        continue
    else:
        if op == "1":
            print("sua operação é soma.")
            n1 = int(input("Digite seu primeiro número: "))
            n2 = int(input("Digite outro número: "))
            print(f"O resultado da sua operação é {n1 + n2}.")
        elif op == "2":
            print("sua operação é subtração.")
            n1 = int(input("Digite seu primeiro número: "))
            n2 = int(input("Digite outro número: "))
            print(f"O resultado da sua operação é {n1 - n2}.")
        elif op == "3":
            print("sua operação é multiplicação.")
            n1 = int(input("Digite seu primeiro número: "))
            n2 = int(input("Digite outro número: "))
            print(f"O resultado da sua operação é {n1 * n2}.")
        elif op == "4":
            print("sua operação é divisão.")
            n1 = int(input("Digite seu primeiro número: "))
            n2 = int(input("Digite outro número: "))
            print(f"O resultado da sua operação é {n1 / n2}.")
        elif op == "5":
            print("sua operação é elevar um número ao quadrado.")
            n1 = int(input("Digite seu número: "))
            print(f"O resultado da sua operação é {n1 * n1}.")
        else:
            break
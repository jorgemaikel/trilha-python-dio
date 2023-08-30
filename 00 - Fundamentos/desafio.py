menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(" Aviso ".center(42, "="), "\n\n", "Depósito realizado com sucesso!", "\n")
            print("=".center(42, "="))

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: R$ "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print(f"Operação falhou! Você não tem saldo suficiente. Seu saldo atual é R$ {saldo:.2f}.")

        elif excedeu_limite:
            print(f"Operação falhou! O valor do saque excede o limite de R$ {limite}.")

        elif excedeu_saques:
            print(f"Operação falhou! Número máximo de saques excedido. Você realizou {LIMITE_SAQUES} operações.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(" Aviso ".center(42, "="), "\n\n", f"Você sacou R$ {valor:.2f}.", "\n")
            print("=".center(42, "="))

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print(" EXTRATO ".center(42, "="), "\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}", "\n")
        print("=".center(42, "="))

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

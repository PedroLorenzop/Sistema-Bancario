menu = "[1] Depositar\n[2] Sacar\n[3] Extrato\n[4] Sair\nEscolha:"

saldo = 0
limite = 500
extrato = ""
numerroSaque = 0
LIMITESAQUE = 3

while True:
    opcao = int(input(menu))
    if opcao == 1:
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            print("Depósito máximo diário atingido!")
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor inválido!")
    elif opcao == 2:
        if numerroSaque >= LIMITESAQUE:
            print("Limite de saques diários atingido!")
        else:
            valor = float(input("Digite o valor do saque: "))
            if valor > saldo + limite:
                print("Saldo insuficiente!")
            else:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numerroSaque += 1
    elif opcao == 3:
        print(f"Saldo: R$ {saldo:.2f}\nLimite: R$ {limite:.2f}\n{extrato}")
    elif opcao == 4:
        break
    else:
        print("Opção inválida!")
    print("-" * 40)
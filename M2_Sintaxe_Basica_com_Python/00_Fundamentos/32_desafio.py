menu = """
    ===== MENU =====

    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [0] - Sair

    ================

> Digite uma opção: """

saldo = 0
limite = 500
extrato = ""
quantidade_saques = 0
limite_saques = 3
quantidade_saques_disponiveis = 0

while True:

    opcao = input(menu)

    if opcao == "1": # Depositar
        valor_deposito = float(input("Digite o valor do depósito: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito de R$ {valor_deposito:.2f}\n"
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")
        else:
            print("O valor informado é inválido!")
    
    elif opcao == "2": # Sacar
        valor_saque = float(input("Digite o valor do saque: "))
        
        excedeu_limite = valor_saque > saldo + limite
        excedeu_saques = quantidade_saques <= limite_saques
        
        #if excedeu_saldo:
        #    print("Saldo insuficiente!")

        if valor_saque > 0:
            if valor_saque <= (saldo + limite) and quantidade_saques < limite_saques:
                saldo -= valor_saque
                extrato += f"Saque de R$ {valor_saque:.2f}\n"
                quantidade_saques += 1
                quantidade_saques_disponiveis = limite_saques - quantidade_saques
                print("Saque realizado com sucesso!")
                print(f"Quantidade total de saques realizados: {quantidade_saques}")
                print(f"Quantidade de saques permitidos: {limite_saques}")
                print(f"Quantidade de saques disponíveis: {quantidade_saques_disponiveis}")
                print("$$$ ATENÇÃO você está utilizando o limite da sua conta $$$" if saldo < 0 else "")

            elif excedeu_limite:
                print("O valor do saque excedeu o saldo + limite da sua conta!")

            elif excedeu_saques:
                print("Limite de saques diários atingido!")
        
        else:
            print("O valor informado é inválido!")
    
    elif opcao == "3": # Extrato
        print("\n #### EXTRATO ####")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print(f"Quantidade total de saques realizados: {quantidade_saques}")
        print(f"Quantidade de saques permitidos: {limite_saques}")
        print(f"Quantidade de saques disponíveis: {quantidade_saques_disponiveis}")
        print("$$$ ATENÇÃO você está utilizando o limite da sua conta $$$" if saldo < 0 else "")
    
    elif opcao == "0":
        print("Você escolheu a opção sair. \nObrigado por usar nosso sistema! \n")
        break
    
    else:
        print("Opção inválida! \nDigite uma opção válida!")
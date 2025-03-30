import textwrap # Esta biblioteca é utilizada para formatar o textos no console
#dedent = textwrap.dedent # Esta função remove a identação de um texto

# PRINTs que reportam operação REALIZADA >> MENSAGEM <<
# PRINTs que reportam operação NÃO REALIZADA ** MENSAGEM **


# A Função deve recebe os argumentos somente por posição
def depositar(saldo, extrato, /):
    valor_deposito = float(input("Digite o valor do depósito: "))

    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito de R$ {valor_deposito:.2f}\n"
        print(f"\n>> Depósito de R$ {valor_deposito:.2f} realizado com sucesso! <<")
    else:
        print("\n** O valor informado é inválido! **")
    
    return saldo, extrato


# A Função deve recebe os argumentos somente por chave-valor
def sacar(*, saldo, extrato, LIMITE, quantidade_saques, LIMITE_SAQUES, quantidade_saques_disponiveis):
    valor_saque = float(input("Digite o valor do saque: "))
    
    excedeu_limite = valor_saque > saldo + LIMITE
    excedeu_saques = quantidade_saques <= LIMITE_SAQUES
    
    if valor_saque > 0:
        if valor_saque <= (saldo + LIMITE) and quantidade_saques < LIMITE_SAQUES:
            saldo -= valor_saque
            extrato += f"Saque de R$ {valor_saque:.2f}\n"
            quantidade_saques += 1
            quantidade_saques_disponiveis = LIMITE_SAQUES - quantidade_saques
            print("\n>> Saque realizado com sucesso! <<")
            print(f"Quantidade total de saques realizados: {quantidade_saques}")
            print(f"Quantidade de saques permitidos: {LIMITE_SAQUES}")
            print(f"Quantidade de saques disponíveis: {quantidade_saques_disponiveis}")
            print("$$$ ATENÇÃO você está utilizando o limite da sua conta $$$" if saldo < 0 else "")

        elif excedeu_limite:
            print("\nO valor do saque excedeu o saldo + limite da sua conta!"
            "\n** Saque não realizado. **")

        elif excedeu_saques:
            print("\n ** Limite de saques diários atingido! **"
            "\n ** Saque não realizado. **")
    
    else:
        print("\n** O valor informado é inválido! **")

    return saldo, extrato, quantidade_saques, quantidade_saques_disponiveis


# A Função recebe os argumentos por posição "/" e por chave-valor "*"
# Exemplo com as 3 possibilidades de como podemos passar os argumentos para a função:
#def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
# pos1, pos2 >> somente por posição (positional only)
# pos_or_kwd >> posição ou chave-valor
# kwd1, kwd2 >> somente por chave-valor (keyword only)
def exibir_extrato(saldo, /, *, extrato, quantidade_saques, LIMITE_SAQUES, quantidade_saques_disponiveis):
    print("\n #### EXTRATO ####")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print(f"Quantidade total de saques realizados: {quantidade_saques}")
    print(f"Quantidade de saques permitidos: {LIMITE_SAQUES}")
    print(f"Quantidade de saques disponíveis: {quantidade_saques_disponiveis}")
    print("$$$ ATENÇÃO você está utilizando o limite da sua conta $$$" if saldo < 0 else "")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n** Usuário já cadastrado com esse CPF. **")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("\n>> Usuário cadastrado com sucesso! <<")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def listar_usuarios(usuarios):
    if usuarios:
        for usuario in usuarios:
            linha = f"""\
                Nome: {usuario['nome']}
                Data Nascimento: {usuario['data_nascimento']}
                CPF: {usuario['cpf']}
                Endereço: {usuario['endereco']}
            """
            print("=" * 50)
            print(textwrap.dedent(linha))
    else:
        print("\n** Ainda não existem usuários cadastrados! **"
        "\nCadastre um novo usuário de acordo com a opção do menu."
        )


def criar_conta(AGENCIA, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n>> Conta criada com sucesso! <<")
        return {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario}

    print("\n** Usuário não encontrado! Cadastre um usuário antes de criar a conta. **")


def listar_contas(contas):
    if contas:
        for conta in contas:
            linha = f"""\
                Agência:\t{conta['agencia']}
                Número Conta:\t\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
            """
            print("=" * 50)
            print(textwrap.dedent(linha))
    else:
        print("\n** Ainda não existem contas cadastradas! **"
        "\nCadastre uma nova conta de acordo com a opção do menu."
        "\nATENÇÃO: Para criar a conta você também precisa ter um usuário cadastrado."
        )


def menu():
    menu = """\n
        ========== MENU ==========

        [1]\tDepositar
        [2]\tSacar
        [3]\tExtrato
        [4]\tNovo Usuário
        [5]\tListar Usuários
        [6]\tNova Conta
        [7]\tListar Contas
        [0]\tSair

        ==========================

    > Digite uma opção: """
    #return input(menu)
    return input(textwrap.dedent(menu))
    


def main():
    AGENCIA = "0001" # Constante
   
    saldo = 0
    extrato = ""
    LIMITE = 500 # Constante
    quantidade_saques = 0
    LIMITE_SAQUES = 3 # Constante
    quantidade_saques_disponiveis = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1": # Depositar

            saldo, extrato = depositar(saldo, extrato)
        
        elif opcao == "2": # Sacar
            saldo, extrato, quantidade_saques, quantidade_saques_disponiveis = sacar(
                saldo = saldo,
                extrato = extrato,
                LIMITE = LIMITE,
                quantidade_saques = quantidade_saques,
                LIMITE_SAQUES = LIMITE_SAQUES,
                quantidade_saques_disponiveis = quantidade_saques_disponiveis,
            )
        
        # Não precisa criar variáveis para receber o return, somente enviar os parâmetros para a função.
        elif opcao == "3": # Extrato
            exibir_extrato(
                saldo,
                extrato = extrato,
                quantidade_saques = quantidade_saques,
                LIMITE_SAQUES = LIMITE_SAQUES,
                quantidade_saques_disponiveis = quantidade_saques_disponiveis,
            )

        elif opcao == "4": # Novo Usuário
            criar_usuario(usuarios)

        elif opcao == "5": # Listar Usuários (Opcional)
            listar_usuarios(usuarios)

        elif opcao == "6": # Nova Conta
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "7": # Listar Conta
            listar_contas(contas)
        
        elif opcao == "0":
            print("Você escolheu a opção sair. \nObrigado por usar nosso sistema! \n")
            break
        
        else:
            print("Opção inválida! \nDigite uma opção válida!")


main()

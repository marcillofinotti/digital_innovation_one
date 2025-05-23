import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta: # Classe Pai
    def __init__(self, numero, cliente):
        self._saldo = 0 # Atributo Privado
        self._numero = numero # Atributo Privado
        self._agencia = "0001" # Atributo Privado
        self._cliente = cliente # Atributo Privado
        self._historico = Historico() # Atributo Privado

    @classmethod # Método de Classe que retorna uma nova instância da classe (Conta)
    def nova_conta(cls, cliente, numero,saldo):
        return cls(numero, cliente, saldo)

    @property # Atributo Privado
    def saldo(self):
        return self._saldo

    @property
    def numero(self): # Atributo Privado
        return self._numero

    @property
    def agencia(self): # Atributo Privado
        return self._agencia

    @property
    def cliente(self): # Atributo Privado
        return self._cliente

    @property
    def historico(self): # Atributo Privado
        return self._historico
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"\n>>> Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("\n** O valor informado é inválido! **")
            return False
        
        return True


class ContaCorrente(Conta): # Classe Filha
    def __init__(self, numero, cliente, saldo, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
        self._saldo = saldo

    def sacar(self, valor):
        quantidade_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._saldo + self._limite
        print(f"Saldo: {self._saldo}; Limite: {self._limite}")
        excedeu_saques = quantidade_saques >= self._limite_saques
        
        if valor > 0:
            if valor <= (self._saldo + self._limite) and quantidade_saques < self._limite_saques:
                self._saldo -= valor
                quantidade_saques += 1
                quantidade_saques_disponiveis = self._limite_saques - quantidade_saques
                print("\n>>> Saque realizado com sucesso!")
                print(f"Quantidade total de saques realizados: {quantidade_saques}")
                print(f"Quantidade de saques permitidos: {self._limite_saques}")
                print(f"Quantidade de saques disponíveis: {quantidade_saques_disponiveis}")
                print("$$$ ATENÇÃO você está utilizando o limite da sua conta. $$$" if self._saldo < 0 else "")
                return True

            elif excedeu_limite:
                print("\nO valor do saque excedeu o saldo + limite da sua conta!"
                "\n** Saque não realizado. **")
                return False

            elif excedeu_saques:
                print("\n ** Limite de saques diários atingido! **"
                "\n ** Saque não realizado. **")
                return False
        
        else:
            print("\n** O valor informado é inválido! **")
            return False

    def __str__(self):
        return f"""\
                Agência:\t{self.agencia}
                C/C:\t\t{self.numero}
                Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )


class Transacao(ABC): # Classe ABSTRATA
    @property
    #@abstractproperty
    def valor(self):
        pass

    #@abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


def menu():
    menu = """\n
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNovo cliente
    [5]\tNova conta
    [6]\tListar contas
    
    [0]\tSair
    
    > Digite uma opção: """
    return input(textwrap.dedent(menu))


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n*** Cliente não possui conta! ***")
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]


def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n*** Cliente não encontrado! ***")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n*** Cliente não encontrado! ***")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n*** Cliente não encontrado! ***")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}\n\t{transacao['data']:}"


    print(extrato)
    print(f"\nSaldo em: {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}\n\tR$ {conta.saldo:.2f}")
    print("==========================================")


def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n*** Já existe cliente com esse CPF! ***")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n*** Cliente não encontrado, fluxo de criação de conta encerrado! ***")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta, saldo=0)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")


def listar_contas(contas):
    if not contas:
        print("\n*** Não existem contas cadastradas! ***")
    else:
        for conta in contas:
            print("=" * 50)
            print(textwrap.dedent(str(conta)))
    return


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            depositar(clientes)

        elif opcao == "2":
            sacar(clientes)

        elif opcao == "3":
            exibir_extrato(clientes)

        elif opcao == "4":
            criar_cliente(clientes)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("\n*** Operação inválida, por favor selecione novamente a operação desejada. ***")


main()

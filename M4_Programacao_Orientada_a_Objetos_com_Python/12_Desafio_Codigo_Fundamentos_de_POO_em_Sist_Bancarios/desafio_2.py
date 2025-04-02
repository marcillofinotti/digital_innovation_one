''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''

#TODO: Implemente a classe SistemaBancario:

    # TODO: Inicialize a lista de contas:
    

    # TODO: Crie uma nova conta e adicione à lista de contas:
    

    # TODO: Liste todas as contas no formato "Titular: R$ Saldo":
    

#TODO: Crie uma instância de SistemaBancario:

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

class SistemaBancario():
    def __init__(self):
        self.contas = [] # Inicializa a lista como atributo de instância
    
    def criar_conta(self, titular, saldo):
        conta = ContaBancaria(titular, saldo)
        self.contas.append(conta) # Acessa 'contas' através da instância

    def listar_contas(self):
        informacoes_contas = [] # Inicializa a lista vazia como variável local
        for conta in self.contas:
            informacoes_contas.append(f"{conta.titular}: R$ {conta.saldo}") # Acessa 'contas' através da instância
        print(", ".join(informacoes_contas))
        

sistema = SistemaBancario() # Cria uma instância de SistemaBancario

while True:
    entrada = input().strip()
    if entrada.upper() == "FIM":  
        break
    titular, saldo = entrada.split(", ")
    sistema.criar_conta(titular, int(saldo))

sistema.listar_contas()

"""
Exemplos:
--------------------
Entrada:
João, 500
Maria, 1000
FIM
Saída:
João: R$ 500, Maria: R$ 1000
--------------------
Entrada:
Ana, 150
Bruno, 250
FIM
Saída:
Ana: R$ 150, Bruno: R$ 250
--------------------
Entrada:
Fernando, 50
Gustavo, 75
Helena, 125
FIM
Saída:
Fernando: R$ 50, Gustavo: R$ 75, Helena: R$ 125
"""
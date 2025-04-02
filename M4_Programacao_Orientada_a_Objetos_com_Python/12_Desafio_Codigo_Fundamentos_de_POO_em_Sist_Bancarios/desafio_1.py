"""
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
"""
    # TODO: Inicialize a conta bancária com o nome do titular, saldo 0 e  liste para armazenar as operações realizadas:
    

    # TODO: Implemente o método para realizar um depósito, adicione o valor ao saldo e registre a operação:
        
    
    # TODO: Implemente o método para realizar um saque:
    
        # TODO: Verifique se há saldo suficiente para o saque
         
            # TODO: Subtraia o valor do saldo (valor já é negativo)
            
            # TODO: Registre a operação e retorne a  mensagem de saque negado
            

    # TODO: Crie o método para exibir o extrato da conta e junte as operações no formato correto:
    
class ContaBancaria:
    def __init__(self, nome_titular):
        self.nome_titular = nome_titular
        self.saldo = 0
        self.operacoes = []  # Lista para armazenar as operações realizadas

    def depositar(self, valor):
        self.saldo += valor
        self.operacoes.append(f"+{valor}")  # Registra o depósito
        return True
    
    def sacar(self, valor):
        if self.saldo >= abs(valor):
            self.saldo += valor # Valor já é negativo
            self.operacoes.append(str(valor))  # Registra o saque
            return True
        else:
            self.operacoes.append("Saque não permitido")
            return False

    def extrato(self):
        operacoes_str = ", ".join(self.operacoes)
        print(f"Operações: {operacoes_str}; Saldo: {self.saldo}")


nome_titular = input().strip()  
conta = ContaBancaria(nome_titular)  

entrada_transacoes = input().strip() 
transacoes = [int(valor) for valor in entrada_transacoes.split(",")]  

for valor in transacoes:
    if valor > 0:
        conta.depositar(valor)  
    else:
        conta.sacar(valor)  

conta.extrato()

"""
Exemplos:
--------------------
Entrada:
Maria
100, -50, 200, -300"
Saída:
Operações: +100, -50, +200, Saque não permitido; 
Saldo: 250
--------------------
Entrada:
Carlos
1000, -500, -600
Saída:
Operações: +1000, -500, Saque não permitido; 
Saldo: 500
--------------------
Entrada:
Ana
0, 100
Saída:
Operações: 0, +100; Saldo: 100
"""
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(funcao, a, b):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")

exibir_resultado(somar, 10, 10) # O resultado da operação e = 20
exibir_resultado(subtrair, 10, 10) # O resultado da operação e = 0

op = somar
print(op(10, 10)) # 20
op = subtrair
print(op(10, 10)) # 0
# Atribuir uma função a uma variável é uma característica de linguagens de primeira classe.
# Em Python, as funções são objetos
# Funções são objetos de primeira classe em Python.
# Funções podem ser atribuídas a variáveis, passadas como argumentos e retornadas como valores.
# Funções podem ser armazenadas em listas, tuplas, dicionários e outros objetos.
# Funções podem ser definidas dentro de outras funções.
# Funções podem ser aninhadas.
# Funções podem ser retornadas de outras funções.
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

print(numeros.pop())  # 0
print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

print(numeros.pop())  # 1
print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9}

print(numeros.pop())  # 2
print(numeros)  # {3, 4, 5, 6, 7, 8, 9}

# O método pop remove e retorna um elemento aleatório do conjunto. Se o conjunto estiver vazio, gera um erro.

palavras = {"teste", "python", "teste", "java", "c++"}
print(palavras)  # {'teste', 'python', 'java', 'c++'}

print(palavras.pop())
print(palavras)

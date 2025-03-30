numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.remove(0))
print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

print(numeros.remove(9))
print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8}

# O método remove remove um elemento do conjunto. Se o elemento não existir, gera um erro.
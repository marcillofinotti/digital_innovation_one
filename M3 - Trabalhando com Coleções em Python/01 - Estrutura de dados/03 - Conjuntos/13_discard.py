numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros.discard(1) # Remove o elemento 1 do conjunto
numeros.discard(45) # Não gera erro, pois o elemento 45 não existe no conjunto
numeros.discard(9) # Remove o elemento 9 do conjunto

print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9}

# O método discard remove um elemento do conjunto, caso ele exista. Se o elemento não existir, o conjunto permanece inalterado e NÃO GERA ERRO.

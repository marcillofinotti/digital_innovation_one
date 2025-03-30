sorteio = {1, 23}

sorteio.add(25)  # {1, 23, 25}
print(sorteio)

sorteio.add(42)  # {1, 23, 25, 42}
print(sorteio)

sorteio.add(25)  # {1, 23, 25, 42}
print(sorteio)

# O método add() adiciona um elemento ao conjunto. Se o elemento já existir, ele não será adicionado novamente.

sorteio.add(1)  # {1, 23, 25, 42}
print(sorteio)



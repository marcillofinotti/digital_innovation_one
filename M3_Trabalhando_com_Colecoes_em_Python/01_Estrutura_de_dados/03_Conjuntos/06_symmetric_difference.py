conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.symmetric_difference(conjunto_b)
print(resultado) # {1, 4} >> Diferente do método difference, o método symmetric_difference retorna os elementos que estão em um conjunto, mas não no outro. Ou seja, ele retorna a diferença simétrica entre os conjuntos.

resultado = conjunto_b.symmetric_difference(conjunto_a)
print(resultado) # {1, 4}
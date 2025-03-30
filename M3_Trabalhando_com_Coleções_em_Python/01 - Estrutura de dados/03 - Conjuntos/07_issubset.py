conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issubset(conjunto_b)  # True
print(resultado) # True >> O conjunto_a é um subconjunto de conjunto_b?

resultado = conjunto_b.issubset(conjunto_a)  # False
print(resultado) # False >> O conjunto_b é um subconjunto de conjunto_a?

# O método issubset retorna True se o conjunto A for um subconjunto do conjunto B especificado e False caso contrário. (De acordo com o exemplo acima).

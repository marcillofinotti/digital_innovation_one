conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issuperset(conjunto_b)  # False
print(resultado)

resultado = conjunto_b.issuperset(conjunto_a)  # True
print(resultado)

# O método issuperset retorna True se o conjunto B possuir os mesmos elementos de A e False caso contrário. (De acordo com o exemplo acima).

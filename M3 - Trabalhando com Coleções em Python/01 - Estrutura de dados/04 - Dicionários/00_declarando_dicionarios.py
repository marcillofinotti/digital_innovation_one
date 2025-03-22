pessoa = {"nome": "Marcillo", "idade": 33}
print(pessoa)

pessoa = dict(nome="Marcillo", idade=33)
print(pessoa)

pessoa["telefone"] = "9988-1234"  # {'nome': 'Marcillo', 'idade': 33, 'telefone': '9988-1234'}
print(pessoa)

pessoa["nome"] = "Marcillo_teste"  # {'nome': 'Marcillo_teste', 'idade': 33, 'telefone': '9988-1234'}
print(pessoa)

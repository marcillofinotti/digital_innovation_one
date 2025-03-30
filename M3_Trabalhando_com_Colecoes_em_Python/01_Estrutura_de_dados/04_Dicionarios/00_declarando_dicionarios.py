pessoa = {"nome": "Marcelo", "idade": 33}
print(pessoa)

pessoa = dict(nome="Marcelo", idade=33)
print(pessoa)

pessoa["telefone"] = "9988-1234"  # {'nome': 'Marcelo', 'idade': 33, 'telefone': '9988-1234'}
print(pessoa)

pessoa["nome"] = "Marcelo_teste"  # {'nome': 'Marcelo_teste', 'idade': 33, 'telefone': '9988-1234'}
print(pessoa)

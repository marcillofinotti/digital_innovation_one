contato = {"nome": "Marcillo", "telefone": "9988-1234"}

contato.setdefault("nome", "Giovanna")  # "Guilherme"
print(contato)  # {'nome': 'Marcillo', 'telefone': '9988-1234'}

contato.setdefault("idade", 33)  # 28
print(contato)  # {'nome': 'Marcillo', 'telefone': '9988-1234', 'idade': 33}

# O método setdefault() retorna o valor da chave especificada. Se a chave não existir, insere a chave com o valor especificado.

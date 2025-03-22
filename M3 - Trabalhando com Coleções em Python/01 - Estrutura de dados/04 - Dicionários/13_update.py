contatos = {"marcillo@gmail.com": {"nome": "Marcillo", "telefone": "9988-1234"}}

print(contatos)
contatos.update({"marcillo@gmail.com": {"nome": "Marc"}})
print(contatos)  # {'marcillo@gmail.com': {'nome': 'Marc'}}

contatos.update({"mariana@gmail.com": {"nome": "Mariana", "telefone": "4444-7766"}})
print(contatos) # {'marcillo@gmail.com': {'nome': 'Marc'}, 'mariana@gmail.com': {'nome': 'Mariana', 'telefone': '4444-7766'}}

# O método update() atualiza um dicionário com itens de outro dicionário ou com um iterável de pares chave-valor.
# Se a chave já existir, o valor será atualizado. Se a chave não existir, será adicionada.
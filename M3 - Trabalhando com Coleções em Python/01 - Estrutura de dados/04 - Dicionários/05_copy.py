contatos = {"marcillo@gmail.com": {"nome": "Marcillo", "telefone": "9988-1234"}}

copia = contatos.copy()
copia["marcillo@gmail.com"] = {"nome": "Marc"}

print(contatos["marcillo@gmail.com"])  # {'nome': 'Marcillo', 'telefone': '9988-1234'}

print(copia["marcillo@gmail.com"])  # {'nome': 'Marc'}

# O método copy() retorna uma cópia de um dicionário.

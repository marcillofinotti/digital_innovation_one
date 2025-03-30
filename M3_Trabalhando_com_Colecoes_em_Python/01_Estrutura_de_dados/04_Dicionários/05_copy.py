contatos = {"marcelo@gmail.com": {"nome": "Marcelo", "telefone": "9988-1234"}}

copia = contatos.copy()
copia["marcelo@gmail.com"] = {"nome": "Marc"}

print(contatos["marcelo@gmail.com"])  # {'nome': 'Marcelo', 'telefone': '9988-1234'}

print(copia["marcelo@gmail.com"])  # {'nome': 'Marc'}

# O método copy() retorna uma cópia de um dicionário.

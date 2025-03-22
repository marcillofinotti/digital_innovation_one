contatos = {"marcillo@gmail.com": {"nome": "Marcillo", "telefone": "9988-1234"}}

# contatos["chave"]  # KeyError

resultado = contatos.get("chave")  # None
print(resultado)

resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get(
    "marcillo@gmail.com", {}
)  # {'nome': 'Marcillo', 'telefone': '9988-1234'}
print(resultado)

# O método get() retorna o valor de uma chave de um dicionário, caso a chave não exista, retorna None ou um valor padrão.
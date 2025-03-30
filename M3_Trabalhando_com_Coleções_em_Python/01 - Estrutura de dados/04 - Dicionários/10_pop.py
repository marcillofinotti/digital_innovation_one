contatos = {"marcelo@gmail.com": {"nome": "Marcelo", "telefone": "9988-1234"}}

resultado = contatos.pop("marcelo@gmail.com")  # {'nome': 'Marcelo', 'telefone': '9988-1234'}
print(resultado)

resultado = contatos.pop("marcelo@gmail.com", {})  # {}
print(resultado)

# O método pop() remove um item de um dicionário e retorna o valor removido. Caso a chave não exista, retorna um valor padrão.
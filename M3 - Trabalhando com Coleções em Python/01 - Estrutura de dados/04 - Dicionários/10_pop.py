contatos = {"marcillo@gmail.com": {"nome": "Marcillo", "telefone": "9988-1234"}}

resultado = contatos.pop("marcillo@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)

resultado = contatos.pop("marcillo@gmail.com", {})  # {}
print(resultado)

# O método pop() remove um item de um dicionário e retorna o valor removido. Caso a chave não exista, retorna um valor padrão.
contatos = {
    "marcelo@gmail.com": {"nome": "Marcelo", "telefone": "9988-1234"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "jose@gmail.com": {"nome": "José", "telefone": "7766-6543"},
    "mariana@gmail.com": {"nome": "Mariana", "telefone": "4444-7766"},
}

del contatos["marcelo@gmail.com"]["telefone"]
del contatos["jose@gmail.com"]


print(contatos) # {'marcelo@gmail.com': {'nome': 'Marcelo'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'}, 'mariana@gmail.com': {'nome': 'Mariana', 'telefone': '4444-7766'}}

# O método del remove um item de um dicionário.
# O método del também pode ser usado para remover um dicionário inteiro.
contatos = {
    "marcelo@gmail.com": {"nome": "Marcelo", "telefone": "9988-1234"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "jose@gmail.com": {"nome": "José", "telefone": "7766-6543"},
    "mariana@gmail.com": {"nome": "Mariana", "telefone": "4444-7766"},
}

resultado = (
    contatos.values()
)  # dict_values([{'nome': 'Marcelo', 'telefone': '9988-1234'}, {'nome': 'Giovanna', 'telefone': '3443-2121'}, {'nome': 'José', 'telefone': '7766-6543'}, {'nome': 'Mariana', 'telefone': '4444-7766'}])
print(resultado)

# O método values() retorna uma visão de todos os valores em um dicionário.

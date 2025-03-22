contatos = {
    "marcillo@gmail.com": {"nome": "Marcillo", "telefone": "9988-1234"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "jose@gmail.com": {"nome": "José", "telefone": "7766-6543"},
    "mariana@gmail.com": {"nome": "Mariana", "telefone": "4444-7766", "extra": {"celular": "9999-8888"}},
}

contato = contatos["mariana@gmail.com"] # {'nome': 'Mariana', 'telefone': '4444-7766', 'extra': {'celular': '9999-8888'}}
print(contato)

#Acessando um dicionário aninhado
telefone = contatos["mariana@gmail.com"]["extra"]  # {'celular': '9999-8888'}
telefone2 = contatos["mariana@gmail.com"]["extra"]["celular"]  # '9999-8888'
print(telefone)
print(telefone2)

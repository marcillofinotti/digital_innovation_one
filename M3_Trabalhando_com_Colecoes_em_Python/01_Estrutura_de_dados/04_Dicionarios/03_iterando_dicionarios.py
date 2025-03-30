contatos = {
    "marcelo@gmail.com": {"nome": "Marcelo", "telefone": "9988-1234"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "jose@gmail.com": {"nome": "José", "telefone": "7766-6543"},
    "mariana@gmail.com": {"nome": "Mariana", "telefone": "4444-7766", "extra": {"celular": "9999-8888"}},
}

for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

for chave, valor in contatos.items():
    print(chave, valor)

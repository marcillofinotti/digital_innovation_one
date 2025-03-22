contatos = {
    "marcillo@gmail.com": {"nome": "Marcillo", "telefone": "9988-1234"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "jose@gmail.com": {"nome": "José", "telefone": "7766-6543"},
    "mariana@gmail.com": {"nome": "Mariana", "telefone": "4444-7766"},
}

resultado = "marcillo@gmail.com" in contatos  # True
print(resultado)

resultado = "joao@gmail.com" in contatos  # False
print(resultado)

resultado = "idade" in contatos["marcillo@gmail.com"]  # False
print(resultado)

resultado = "telefone" in contatos["mariana@gmail.com"]  # True
print(resultado)

# O método in verifica se a chave existe no dicionário.
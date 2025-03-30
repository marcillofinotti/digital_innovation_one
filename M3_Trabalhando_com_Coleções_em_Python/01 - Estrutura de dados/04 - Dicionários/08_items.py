contatos = {"marcelo@gmail.com": {"nome": "Marcelo", "telefone": "9988-1234"},
            "mariana@gmail.com": {"nome": "Mariana", "telefone": "4444-7766", "extra": {"celular": "9999-8888"}}
            }

resultado = contatos.items()
print(resultado)

# O método items() retorna uma lista de tuplas, onde cada tupla contém um par chave-valor do dicionário.
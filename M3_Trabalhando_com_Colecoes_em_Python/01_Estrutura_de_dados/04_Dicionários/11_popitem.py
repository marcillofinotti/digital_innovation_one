contatos = {"marcelo@gmail.com": {"nome": "Marcelo", "telefone": "9988-1234"},
            "marcelo2@gmail.com": {"nome": "Marcelo", "telefone": "9988-1234"}
            }

resultado = contatos.popitem()  # "marcelo@gmail.com": {"nome": "Marcelo", "telefone": "9988-1234"}
print(resultado)

resultado = contatos.popitem() # ('marcelo@gmail.com', {'nome': 'Marcelo', 'telefone': '9988-1234'})
print(resultado)

# resultado = contatos.popitem() # KeyError
# print(resultado)

# O método popitem() remove o último item inserido em um dicionário e retorna uma tupla com a chave e o valor removido.
# A diferença entre o método pop() e o método popitem() é que o método pop() recebe uma chave como argumento e o método popitem() não recebe argumentos.
# O método pop() retorna o valor removido e o método popitem() retorna uma tupla com a chave e o valor removido.
# Se a chave não existir, o método pop() retorna um valor padrão e o método popitem() lança uma exceção KeyError.

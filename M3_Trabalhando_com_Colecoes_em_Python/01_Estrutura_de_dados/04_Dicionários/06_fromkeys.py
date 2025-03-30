resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado)

resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
print(resultado)

# O método fromkeys() cria um novo dicionário com as chaves especificadas e o valor padrão None.
# Se você quiser definir um valor padrão diferente de None, você pode passar um segundo argumento.

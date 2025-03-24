def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Quarta, 12 mar 2025", "Zen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)
# "*args" parâmetros posicionais.
# "**kwargs" parâmetros nomeados.


"""
def exibir_poema(data_extenso, *tupla, **dicionario):
    # "*" é usado para passar argumentos posicionais variáveis (dentro de uma tupla).
    # "**" é usado para passar argumentos nomeados variáveis (dentro de um dicionário).
    texto = "\n".join(tupla)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dicionario.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Quarta, 12 mar 2025", "Zen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)"
"""
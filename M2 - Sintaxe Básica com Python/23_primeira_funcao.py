def exibir_mensagem():
    print("Olá, mundo!")


def exibir_mensagem_2(nome):
    print(f"Seja bem-vindo, {nome}!")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem-vindo, {nome}!")


exibir_mensagem()
exibir_mensagem_2(nome="Marcillo") # Não é necessário passar o nome do parâmetro, pode informar direto.
exibir_mensagem_2("Marcillo")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")
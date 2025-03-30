while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break # interrompe a execução do laço

    if numero % 2 == 0: # se o número for par
        continue # pula para a próxima iteração

    print(numero)


# for numero in range(100):

#     if numero % 2 == 0:
#         continue # pula para a próxima iteração

#     print(numero, end=" ")
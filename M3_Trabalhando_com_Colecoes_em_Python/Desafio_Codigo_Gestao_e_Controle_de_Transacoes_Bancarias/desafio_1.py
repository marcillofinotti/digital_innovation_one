def calcular_saldo(transacoes):
    saldo = 0

    # TODO: Itere sobre cada transação na lista:
    
        # TODO: Adicione o valor da transação ao saldo
        

    # TODO: Retorne o saldo formatado em moeda brasileira com duas casas decimais:

    for numero in transacoes:
        saldo += numero
        
    #return float(saldo)
    return round(saldo, 2) # Arredonda o saldo para duas casas decimais
    

#entrada_usuario = input("Digite alguns valores inteiros ou decimais: ") # Não pode ter esta mensagem para testar e enviar o código.
entrada_usuario = input()

entrada_usuario = entrada_usuario.strip("[]").replace(" ", "")

transacoes = [float(valor) for valor in entrada_usuario.split(",")]

# TODO: Calcule o saldo com base nas transações informadas:
resultado = calcular_saldo(transacoes)

#print(f"Saldo: R$ {resultado:.2f}")
print(f"Saldo: R$ {resultado:.2f}")
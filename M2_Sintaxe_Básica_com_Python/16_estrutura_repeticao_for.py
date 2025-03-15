texto = input("Informe um texto: ")
VOGAIS = "AEIOU"


# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        #print(letra, end="") # end >> escreve na mesma linha
        print(letra.upper(), end="")
else:
    print()  # adiciona uma quebra de linha


# Exemplo utilizando a função built-in range
# range(start, stop, step) -> range object
for numero in range(0, 51, 5):
    print(numero, end=" ")
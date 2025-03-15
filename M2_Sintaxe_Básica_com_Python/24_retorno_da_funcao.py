def calcular_total(numeros):
    return sum(numeros)

def retorna1_antecessor_e_sucessor(numero): # Forma idel de escrita do código
    return numero - 1, numero + 1

def retorna2_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

def func_3():
    print("Olá mundo!")

print(calcular_total([10, 20, 34])) # 64
print(retorna1_antecessor_e_sucessor(10)) # (9, 11)
print(retorna2_antecessor_e_sucessor(10)) # (9, 11)
print(func_3()) # None
# None é retornado quando a função não tem um return explícito.
# Se a função não tiver um return explícito, ela retornará None.
# Se a função tiver um return explícito, ela retornará o valor retornado.
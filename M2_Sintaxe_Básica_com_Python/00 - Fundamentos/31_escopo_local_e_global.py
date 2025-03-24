salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

salario_com_bonus = salario_bonus(500) # 2500
print(salario_com_bonus)

# Observar o uso de objetos mutáveis (lista) que precisam ser copiados para evitar alterações indesejadas.
salario = 3000

def salario_bonus(bonus, lista):
    global salario
    
    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"Lista Auxiliar = {lista_aux}")

    salario += bonus
    return salario

lista = [1]
salario_com_bonus = salario_bonus(500, lista) # 3500
print(salario_com_bonus)
print(f"Lista Original = {lista}") # [1]
nome = "Marcillo"
idade = 33
profissao = "programador"
linguagem = "Python"
saldo = 55.545

dados = {"nome": "Marcillo", "idade": 33}

#Usado no Python 2
print("Nome: %s, Idade: %d" % (nome, idade))

#Usado no Python 3
print("Nome: {}, Idade: {}".format(nome, idade))
print("Nome: {0}, Idade: {1}".format(nome, idade))
print("Nome: {1}, Idade: {0}".format(idade, nome))
print("Nome: {1}, Idade: {0} Nome: {1} {1}".format(idade, nome))

print("Nome: {nome}, Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name}, Idade: {age} {name} {name} {age}".format(age=idade, name=nome))

print("Nome: {nome}, Idade: {idade}".format(**dados))

print(f"Nome: {nome}, Idade: {idade}")
print(f"Nome: {nome}, Idade: {idade} Saldo: {saldo}")
print(f"Nome: {nome}, Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome: {nome}, Idade: {idade} Saldo: {saldo:.1f}")


PI = 3.14159
print(f"Valor de PI: {PI:.2f}")

print(f"Valor de PI: {PI:10.2f}")

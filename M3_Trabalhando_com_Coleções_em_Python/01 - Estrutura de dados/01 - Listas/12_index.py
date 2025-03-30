linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.index("java"))  # 3 
print(linguagens.index("python"))  # 0

linguagens = ["python", "kotlin", "js", "c", "java", "csharp", "kotlin", "c"]
print(linguagens.index("kotlin"))  # 1 >> o método index() retorna o índice do primeiro elemento encontrado na lista
print(linguagens.index("c"))  # 1

linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"] >> sorted() retorna uma nova lista ordenada
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]

print(linguagens[0])  # ["python", "js", "c", "java", "csharp"] >> a lista original não é alterada

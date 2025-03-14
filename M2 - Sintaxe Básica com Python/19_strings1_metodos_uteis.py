nome = "mARciLlo"

print(nome.upper()) # MARCILLO
print(nome.lower()) # marcillo
print(nome.capitalize()) # Marcillo
print(nome.title()) # Marcillo

texto = "  Olá mundo!    "

print(texto + ".") #   Olá mundo!
print(texto.strip() + ".") # Olá mundo!
print(texto.rstrip() + ".") #   Olá mundo!
print(texto.lstrip() + ".") # Olá mundo!

menu = "Python"

print("####" + menu + "####") # ####Python####
print(menu.center(14)) #    Python
print(menu.center(14, "#")) # ####Python####

print("P-y-t-h-o-n")

for letra in menu:
    print(letra, end="-")
print() # P-y-t-h-o-n-

print("-".join(menu)) # P-y-t-h-o-n
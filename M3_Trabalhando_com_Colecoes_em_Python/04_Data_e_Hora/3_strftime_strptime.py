# Documentação Python:
# https://docs.python.org/3.11/library/datetime.html#strftime-strptime-behavior
# https://docs.python.org/3.11/library/datetime.html#module-datetime
from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2025-03-20 15:20"
mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%Y-%m-%d %H:%M"

aplicar_mascara_ptbr = data_hora_atual.strftime(mascara_ptbr) # Formatando a string
print(aplicar_mascara_ptbr)
print(type(aplicar_mascara_ptbr))

data_convertida_en = datetime.strptime(data_hora_str, mascara_en) # Convertendo a string para datetime
print(data_convertida_en)
print(type(data_convertida_en))

# Formatar string com >> strftime = string format time
# Converter string para datetime com >> strptime = string parse time

import sys
import re

periodos = {}

periodo = r';\d+;(.*?);'

for linha in sys.stdin:
    if "nome" in linha:
        continue

    m = re.search(periodo, linha)
    if m:
        per = m.group(1)
        periodos[per] = periodos.get(per, 0) + 1
    
print("Quantidade de obras por periodo:")
for chave, valor in periodos.items():
    print(f"{chave}: {valor}")

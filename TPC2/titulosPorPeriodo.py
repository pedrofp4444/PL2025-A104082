import sys
import re

periodos = {}

periodoETitulo = r'^(\w.*?);.*\d{4};(.*?);'

for linha in sys.stdin:
    if "nome" in linha:
        continue

    m = re.search(periodoETitulo, linha)
    if m:
        titulo = m.group(1)
        periodo = m.group(2)
        periodos[periodo] = periodos.get(periodo, []) + [titulo]

for chave, valor in periodos.items():
    valor.sort()

print("Titulos por periodo:")
for chave, valor in periodos.items():
    print(f"{chave}: {len(valor)}")
    for titulo in valor:
        print(f"    {titulo}")

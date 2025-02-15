import sys
import re

compositores = []

compositor = r'\d\d\d\d;.*?;(.*?);'

for linha in sys.stdin:
    if "nome" in linha:
        continue
    
    m = re.search(compositor, linha)
    if m:
        compositores.append(m.group(1))

compositores.sort()

print("Compositores ordenados:")
for c in compositores:
    print(c)

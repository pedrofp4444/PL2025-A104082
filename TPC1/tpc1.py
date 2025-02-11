import sys

acc = 0
summing = True

for linha in sys.stdin:
    i = 0
    while i < len(linha):
        if linha[i].isdigit():
            start = i
            while i < len(linha) and linha[i].isdigit():
                i = i + 1
            valor = int(linha[start:i])
            if summing:
                acc = acc + valor
        elif linha[i:i+2].lower() == "on":
            summing = True
            i = i + 2
        elif linha[i:i+3].lower() == "off":
            summing = False
            i = i + 3
        elif linha[i] == '=':
            print(acc)
            i = i + 1
        else:
            i = i + 1

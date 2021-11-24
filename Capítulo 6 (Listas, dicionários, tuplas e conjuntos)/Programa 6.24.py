"""
    Programa 6.24 - Exemplo de dicionário com valor padrão
"""

d = {}

for letra in 'abracadabra':
    d[letra] = d.get(letra, 0) + 1

print(d)

"""
    Programa 8.1 - Pesquisa em uma lista
"""

def pesquise(lista, valor):
    for x, e in enumerate(lista):
        if e == valor:
            return x # 1
    return None # 2

L = [10, 20, 25, 30]
print(pesquise(L, 25))
print(pesquise(L, 27))

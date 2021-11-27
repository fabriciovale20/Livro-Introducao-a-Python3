"""
    Exercício 05

    Reescreva função do Programa 8.1 de forma a utilizar os métodos de pesquisa em lista, vistos no Capítulo 7.
"""

def pesquise(lista, valor):
    return f'{lista.index(valor)}º posição' if valor in lista else 'Valor não encontrato'

L = [10, 20, 25, 30]
print(pesquise(L, 25))
print(pesquise(L, 27))

"""
    Programa 8.14 - Função soma com número indeterminado de parâmetros
"""

def soma(*args):
    s = 0

    for x in args:
        s += x
    return s

soma(1, 2)
soma(2)
soma(5, 6, 7, 8)
soma(9, 10, 20, 30, 40)

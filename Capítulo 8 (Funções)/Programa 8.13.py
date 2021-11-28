"""
    Programa 8.13 - Configuração de funções com funções
"""

def imprime_lista(L, fimpressão, fcondição):
    for e in L:
        if fcondição(e):
            fimpressão(e)

def imprime_elemento(e):
    print(f'Valor: {e}')

def épar(x):
    return x % 2 == 0

def éimpar(x):
    return not épar(x)

L = [1, 7, 9, 2, 11, 0]

imprime_lista(L, imprime_elemento, épar)
imprime_lista(L, imprime_elemento, éimpar)

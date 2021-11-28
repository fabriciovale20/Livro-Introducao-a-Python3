"""
    Programa 8.12 - Funções como parâmetro
"""

def soma(a, b):
    return a + b

def subtração(a, b):
    return a - b

def imprime(a, b, foper):
    print(foper(a, b))  # 1

imprime(5, 4, soma) # 2
imprime(10, 1, subtração) # 3

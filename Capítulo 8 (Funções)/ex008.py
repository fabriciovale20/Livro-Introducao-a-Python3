"""
    Exercício 08

    Usando a função do mdc defina no exercício anterior, defina uma função para calcular o menor múltiplo comum (M.M.C) entre dois números.

mmc(a, b) = { |a x b| / mdc(a, b) }

Em que |a x b| pode ser escrito em Python como: abs(a * b).
"""

def mdc(a, b):
    if b == 0:
        return a
    elif a > b:
        return mdc(b, a % b)


def mmc(a, b):
    return abs(a * b) / mdc(a, b)

print(mmc(3, 2))

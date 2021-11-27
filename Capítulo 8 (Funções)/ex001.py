"""
    Exercício 01

    Escreva uma função que retorne o maior de dois números.
Valores esperados:
máximo(5, 6) == 6
máximo(2, 1) == 2
máximo(7, 7) == 7
"""

def máximo(a, b):
    maior = [a, b]
    return max(maior)

print(máximo(5, 6))
print(máximo(2, 1))
print(máximo(7, 7))

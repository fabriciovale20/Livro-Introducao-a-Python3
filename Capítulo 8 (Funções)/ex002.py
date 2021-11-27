"""
    Exercício 02

    Escreva uma função que receba dois números e retorne True se o primeiro número for múltiplo do segundo.
Valores esperados:
múltiplo(8, 4) == True
múltiplo(7, 3) == False
múltiplo(5, 5) == True
"""

def múltiplo(a, b):
    return True if a % b == 0 else False

print(múltiplo(8, 4))
print(múltiplo(7, 3))
print(múltiplo(5, 5))

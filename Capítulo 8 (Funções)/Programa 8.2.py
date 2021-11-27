"""
    Programa 8.2 - Como não escreva uma função
"""

def soma(L):
    total = 0
    x = 0

    while x < 5:    # O problema dessa função "soma" é que só serve para lista de 5 elementos.
        total += L[x]
        x += 1
    return total

L = [1, 7, 2, 9, 15]

print(soma(L))  # 1
print(soma([7, 9, 12, 3, 100, 20, 4]))  # 2

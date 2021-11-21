"""
    Exercício 12

    Altere o Programa 6.11 de forma a imprimir o menor elemento da lista.
"""

L = [1, 7, 2, 4]
máximo = menor = L[0]

for e in L:
    if e > máximo:
        máximo = e
    
    if e < menor:
        menor = e

print(f'Menor: {menor} \nMaior: {máximo}')
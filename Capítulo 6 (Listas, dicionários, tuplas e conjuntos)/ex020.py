"""
    Exercício 20

    Escreva um programa que compare duas listas. Considere a primeira lista como a versão inicial e a segunda como a versão após alterações.
Utilizando operações com conjuntos, seu programa deverá imprimir a lista de modificações entre essas duas versões, listando:
• Os elementos que não mudaram;
• Os novos elementos;
• Os elementos que foram removidos.
"""

versão_inicial = {4, 6, 8 , 10}
versão_alteração = {1, 2, 3, 5, 6, 7, 8, 9, 10}

print('Os elementos que não mudaram: ', end=' ')
for c in versão_alteração:
    if c in versão_inicial:
        print(c, end=' ')
print()

print('Os novos elementos: ', end=' ')
print(versão_alteração - versão_inicial)

print('Os elementos que foram removidos: ', end=' ')
print(versão_inicial - versão_alteração)

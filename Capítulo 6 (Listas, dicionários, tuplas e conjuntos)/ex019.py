"""
    Exercício 19

    Escreva um programa que compare duas listas. Utilizando operações com conjuntos, imprima:
• Os valores comuns às duas listas;
• Os valores que só existem na primeira;
• Os valores que existem apenas na segunda;
• Uma lista com os elementos não repetidos das duas listas;
• A primeira lista sem os elementos repetidos na segunda.
"""

a = [1, 2, 4, 8, 7, 9, 10]
b = [3, 5, 6, 7, 8]

# Os valores comuns às duas listas
print('Os valores comuns às duas listas: ', end='')
for c in b:
    if c in a:
        print(c, end=' ')
print()

# Os valores que só existem na primeira
print('Os valores que só existem na primeira: ', end='')
for c in a:
    if c not in b:
        print(c, end=' ')
print()

# Os valores que existem apenas na segunda
print('Os valores que existem apenas na segunda: ', end='')
for c in b:
    if c not in a:
        print(c, end=' ')
print()

# Uma lista com os elementos não repetidos das duas listas
print('Uma lista com os elementos não repetidos das duas listas: ', end='')
lista_nao_repetidos = []
for c in a:
    if c not in b:
        lista_nao_repetidos.append(c)
print(lista_nao_repetidos)

# A primeira lista sem os elementos repetidos na segunda
print('A primeira lista sem os elementos repetidos na segunda: ', end='')
lista_sem_elementos_segunda = []
for c in a:
    if c not in b:
        lista_sem_elementos_segunda.append(c)
print(lista_sem_elementos_segunda)

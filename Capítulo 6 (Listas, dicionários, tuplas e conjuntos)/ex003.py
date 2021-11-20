"""
    Exercício 03

    Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.
"""

lista_a = [1, 4, 6, 7, 9]
lista_b = [2, 4, 6, 7, 10]

lista_c = []
cont = 0

n = len(lista_a) + len(lista_b)

while cont < len(lista_a):
    if lista_a[cont] not in lista_c:
        lista_c.append(lista_a[cont])
    
    cont += 1

cont = 0

while cont < len(lista_b):
    if lista_b[cont] not in lista_c:
        lista_c.append(lista_b[cont])
    
    cont += 1

print(lista_c)
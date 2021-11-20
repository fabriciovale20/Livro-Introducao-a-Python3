"""
    Exercício 02

    Faça um programa que leia duas listas e que gere uma terceira com os elemnetos das duas primeiras.
"""

lista_a = [1, 3, 5, 7, 9]
lista_b = [2, 4, 6, 8, 10]

# 1º Forma
lista_c = lista_a + lista_b

# 2º Forma
lista_d = []
lista_d.extend(lista_a)
lista_d.extend(lista_b)

print(lista_c)
print()
print(lista_d)

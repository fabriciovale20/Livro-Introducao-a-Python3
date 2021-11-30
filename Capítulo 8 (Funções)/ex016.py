"""
    Exercício 16

    Utilizando a função type, escreva uma função recursiva que imprima os elementos de uma lista. Cada elemento deve ser impresso
separadamente, um por linha. Considere o caso de listas dentro de listas, como L = [1, [2, 3, 4, [5, 6, 7]]].
A cada nível, imprima a lista mais á direita, como fazemos ao indentar blocos em Python, Dica: envie o nível atual como parâmentro e utilize-o
para calcular a quantidade de espaçõs em branco à esquerda de cada elemento.
"""

def imprima_item(lista):
    for c in lista:
        if isinstance(c, list):
            imprima_item(c)
        else:
            print(c)


L = [1, 2, [3, 4, [5, 6, 7, [8, 9, 10]]], 11]
imprima_item(L)

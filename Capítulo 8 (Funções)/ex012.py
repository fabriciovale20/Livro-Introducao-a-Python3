"""
    Exercício 12

    Escreva uma função que receba uma string e uma lista. A função deve comprar a string passada com os elementos da lista, também passada
como parâmetro. Retorne verdadeiro se a string for encontrada dentro da lista, e falso, caso contrário.
"""

def verificar(string, lista):
    return True if string in lista else False

lista = ['Nome', 'python', 'string', 'lista']
print(verificar('python', lista))

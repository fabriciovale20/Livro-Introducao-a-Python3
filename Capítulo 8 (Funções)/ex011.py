"""
    Exercício 11

    Escreva uma função para validar uma variável string. Essa função recebe como parâmetro a string, o número mínimo e máximo de caracteres.
Retorne verdadeiro se o tamanho da string estiver entre os valores e de máximo e mínimo, e falso, caso contrário.
"""

def validar(string, mínimo, máximo):
    caracteres = len(string)

    if caracteres > mínimo and caracteres < máximo:
        return True
    else:
        return False

print(validar('Fabrício', 2, 9))
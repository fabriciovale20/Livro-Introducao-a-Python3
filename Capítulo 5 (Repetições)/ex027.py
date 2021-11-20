"""
    Exercício 27

    Escreva um programa que verifique se um número é palíndromo.
Um número é palíndromo se continua o mesmo caso seus dígitos sejam invertidos.
Exemplos: 454, 10501
"""

n = input('Número: ')
a = n[::-1]

if n == a:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')

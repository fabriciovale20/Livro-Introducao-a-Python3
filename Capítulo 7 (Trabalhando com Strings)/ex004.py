"""
    Exercício 04

    Escreva um programa que leia uma string e imprima quantas vezes cada caractere aparece nessa string.
String: TTAAC
Resultado:
T: 2x
A: 2x
C: 1x
"""

string = 'TTAAC'

string_set = set(string)

for c in string_set:
    print(f'{c}: {string.count(c)}x')
    
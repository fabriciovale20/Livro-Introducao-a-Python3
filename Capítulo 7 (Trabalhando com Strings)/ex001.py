"""
    Exercício 01

    Escreva um programa que leia duas strings. Verifique se a segunda ocorre dentro da primeira e imprima a posição de início.
1º string: AABBEFAATT
2º string: BE
Resultado: BE encontrado na posição 3 de AABBEEFAATT
"""

string_a = 'AABBEEFAATT'
string_b = 'BE'

if string_b in string_a:
    print(f'Resultado: {string_b} encontrado na posição {string_a.find(string_b)} de {string_a}')
else:
    print(f'Resultado: {string_b} não foi encontrado em {string_a}')

"""
    Exercício 03

    Escreva um programa que leia duas strings e gere uma terceira apenas com os caracteres que aparecem em uma delas.
1º string: CTA
2º string: ABC
Resultado BT

A ordem dos caracteres da terceira string não é importante.
"""

string_a = 'CTA'
string_b = 'ABC'
string_c = ''

for c in string_b:
    if c not in string_a:
        string_c += c

for c in string_a:
    if c not in string_b:
        string_c += c

print(f'Resultado: {string_c}')

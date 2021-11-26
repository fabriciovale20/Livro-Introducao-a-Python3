"""
    Exercício 05

    Escreva um programa que leia duas strings e gere uma terceira, na qual os caracteres da segunda foram retirados da primeira.
1º string: AATTGGAA
2º string: TG
3º string: AAAA
"""

string_a = 'AATTGGAA'
string_b = 'TG'
string_c = ''

for c in string_a:
    if c not in string_b:
        string_c += c
print(string_c)

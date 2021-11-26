"""
    Exercício 02

    Escreva um programa que leia duas strings e gere uma terceira com os caracteres comuns às duas strings lidas.
1º string: AAACTBF
2º string: CBT
Resultado: CBT

A ordem dos caracteres da string gerada não é importante, mas deve conter todas as letras comuns a ambas.
"""

string_a = 'AAACTBF'
string_b = 'CBT'
string_c = ''

for c in string_b:
    if c in string_a:
        string_c += c

print(f'Resultado: {string_c}')

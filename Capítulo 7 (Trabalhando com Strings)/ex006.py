"""
    Exercício 06

    Escreva um programa que leia três strings. Imprima o resultado da substituição na primeira, dos caracteres da segunda pelos da terceira.
1º string: AATTCGAA
2º string: TG
3º string: AC
Resultado: AAAACCAA
"""

string_a = 'AATTCGAA'
string_a = list(string_a)

string_b = 'TG'
string_c = 'AC'


for c in range(0, (len(string_a)-1)):
    if string_b[0] == string_a[c]:
        string_a[c] = string_c[0]
    elif string_b[1] == string_a[c]:
        string_a[c] = string_c[1]

resultado = ''.join(string_a)
print(resultado)

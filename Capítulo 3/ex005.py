"""
    Exercício 05

    Calcule o resultado da expressão A > B and C or D, utilizando os valores da tabela a seguir:
    A       B        C       D        Resultado
1º  1       2       True    False       False
2º  10      3       False   False       False
3º  5       1       True    True        True
"""

# 1º expressão
a = 1
b = 2
c = True
d = False
print(f'1º Expressão: {a > b and c or d}')

# 2º expressão
a = 10
b = 3
c = False
d = False
print(f'2º Expressão: {a > b and c or d}')

# 3º expressão
a = 5
b = 1
c = True
d = True
print(f'3º Expressão: {a > b and c or d}')

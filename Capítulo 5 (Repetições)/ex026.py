"""
    Exercício 26

    Escreva um programa que calcule o resto da divisão inteira entre dois números.
Utilize apenas as operações de soma e subtração para calcular o resultado.
"""

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
resto = 0

while a >= b:
    resto = a - b
    a -= b

print(f'\nResto: {resto}')
"""
    Exercício 08

    Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma
e subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles.
Assim, 4 x 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.
"""

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
contagem = 1
soma = 0

print(f'{a} x {b}')

while contagem <= b:
    if contagem != b:
        print(a, end=' + ')
    else:
        print(a, end=' = ')

    contagem = contagem + 1
    soma = soma + a

print(soma)

contagem = 1
soma = 0
while contagem <= a:
    if contagem != b:
        print(b, end=' + ')
    else:
        print(b, end=' = ')

    contagem = contagem + 1
    soma = soma + b

print(soma)

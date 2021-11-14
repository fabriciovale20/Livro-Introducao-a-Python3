"""
    Exercício 03

    Escreva um programa que leia três números e que imprima o maior e o menor.
"""

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

if a == b and b == c and a == c:
    print(f'Os três valores são iguais.')

if a != b or c != b or a != c:
    print('O maior valor é ', end='')

if a > b and a > c:
    print(a)
    print('O menor valor é ', end='')
    if b > c or b == c:
        print(c)
    if c > b:
        print(b)

if b > a and b > c:
    print(b)
    print('O menor valor é ', end='')
    if a > c or a == c:
        print(c)
    if c > a:
        print(a)

if c > a and c > b:
    print(c)
    print('O menor valor é ', end='')
    if a > b or a == b:
        print(b)
    if b > a:
        print(a)

if a == b and a > c:
    print(a)
    print(f'O menor valor é {c}')

if a == c and a > b:
    print(a)
    print(f'O menor valor é {b}')

if b == c and b > a:
    print(b)
    print(f'O menor valor é {a}')
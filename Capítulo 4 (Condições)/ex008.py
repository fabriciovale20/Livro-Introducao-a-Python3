"""
    Exercício 08

    Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.
"""

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))

print('''Qual operação deseja realizar:
1- Soma;
2- Subtração;
3- Multiplicação;
4- Divisão.
Escolha: ''', end='')
opção = int(input(''))

if opção == 1:
    print(f'A soma entre {a} e {b} é igual a {a + b}.')
elif opção == 2:
    print(f'A subtração entre {a} e {b} é igual a {a - b}.')
elif opção == 3:
    print(f'A multiplicação entre {a} e {b} é igual a {a * b}.')
elif opção == 4:
    print(f'A divisão entre {a} e {b} é igual a {a / b}.')
else:
    print(f'Opção inválida, tente novamente.')
    
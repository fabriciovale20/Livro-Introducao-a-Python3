"""
    Exercício 04

    Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
"""

salário = float(input('Salário: R$ '))

if salário > 1250:
    aumento = 10
    salário = salário * 1.1

if salário <= 1250:
    aumento = 15
    salário = salário * 1.15

print(f'Seu salário atual com aumento de {aumento}% é R$ {salário:.2f}.')

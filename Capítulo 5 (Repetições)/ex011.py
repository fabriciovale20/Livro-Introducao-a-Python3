"""
    Exercício 11

    Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses.
Escreva o total ganho com juros no período.
"""

depósito_inicial = float(input('Depósitio inicial: R$ '))
taxa_juros = float(input('Taxa de juros (%): '))

mês = 1

while mês <= 12:
    depósito_inicial = depósito_inicial * (1 + (taxa_juros / 100))

    print(f'Mês {mês}: R$ {depósito_inicial:.2f}')
    mês = mês + 1

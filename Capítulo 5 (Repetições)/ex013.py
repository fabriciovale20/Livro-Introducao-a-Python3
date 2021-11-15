"""
    Exercício 13

    Escreva um programa que pergunte o valor inicial de uma divida e o juros menal. Pergunte também o valor mensal que será pago.
Imprima o número de meses para que a divida seja paga, o total pago o total de juros pago.
"""

valor_inicial_divida = float(input('Valor inicial da divida: R$ '))
juros_mensal = float(input('Juros mensal (%): '))
valor_mensal_pago = float(input('Valor mensal pago: R$ '))

juros = meses = 0
total_pago = valor_inicial_divida

while total_pago > 0:
    juros = (total_pago * (juros_mensal / 100)) + juros
    meses = meses + 1
    total_pago = total_pago + (total_pago * (juros_mensal / 100)) - valor_mensal_pago

print(f'\nTotal pago: R$ {valor_inicial_divida + juros:.2f}')
print(f'Meses: {meses}')
print(f'Juros pago: R$ {juros:.2f}')
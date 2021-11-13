"""
    Exercício 11

    Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
Exiba o valor do desconto e o preço a pagar.
"""

preço_mercadoria = float(input('Preço da mercadoria: R$ '))
percentual_desconto = float(input('Percentual do desconto: '))

preço_atual_mercadoria = preço_mercadoria * (1 + (percentual_desconto / 100))

print(f'\nPreço incial: R$ {preço_mercadoria:.2f}.')
print(f'Percentual do desconto: {percentual_desconto:.2f}%.')
print(f'\nValor da mercadoria com desconto: R$ {preço_atual_mercadoria:.2f}.')

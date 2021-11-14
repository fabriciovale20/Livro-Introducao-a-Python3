"""
    Exercício 09

    Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e
a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor
da casa a comprar dividido pelo número de meses a pagar.
"""

valor_casa = float(input('Valor da casa: R$ '))
salário = float(input('Salário: R$ '))
anos_pagar = int(input('Quantidade de anos a pagar: '))

prestação = valor_casa / (anos_pagar * 12)
valor_30 = salário * 0.3

if prestação > valor_30:
    print(f'Empréstimo não autorizado! Valor da prestação (R$ {prestação:.2f}) maior que 30% do salário (R$ {valor_30:.2f}).')
else:
    print(f'Empréstimo autorizado! Valor das prestações R$ {prestação:.2f} por mês.')

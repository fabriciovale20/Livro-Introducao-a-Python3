"""
    Exercício 10

    Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residência, I para indústria e C para comércios.
Calcule o preço a pagar de acordo com a tabela a seguir:

Preço por tipo e faixa de consumo
Tipo            Faixa (kWh)     Preço
Residencial     Até 500         R$ 0,40
Residencial     Acima de 500    R$ 0,65

Comercial       Até 1000        R$ 0,55
Comercial       Acima de 1000   R$ 0,60

Indústrial      Até 5000        R$ 0,55
Indústrial      Acima de 5000   R$ 0,60
"""

quantidade_kwh = int(input('Quantidade de kWh? '))
print('''Tipos de indústria:
R - Residêncial
I - Indústria
C - Comercial''')
tipo_indústria = input('Qual tipo? ')

if tipo_indústria in 'rR':
    if quantidade_kwh <= 500:
        preço = 0.4
    else:
        preço = 0.65
elif tipo_indústria in 'iI':
    if quantidade_kwh <= 1000:
        preço = 0.55
    else:
        preço = 0.60
elif tipo_indústria in 'cC':
    if quantidade_kwh <= 5000:
        preço = 0.55
    else:
        preço = 0.60
else:
    print('Tipo de indústria inválida, tente novamente.')

if tipo_indústria in 'rRiIcC':
    print(f'''Quantidade de kWh: {quantidade_kwh}
Preço: R$ {preço:.2f}
Valor à pagar: R$ {quantidade_kwh * preço:.2f}''')
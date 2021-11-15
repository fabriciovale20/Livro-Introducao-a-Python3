"""
    Exercício 12

    Altere o programa anterior de forma a perguntar também o valor depositado mensalmente. Esse valor será depositado no início de cada mês,
se você deve considerá-lo para o cálculo de juros do mês seguinte.
"""

depósito_inicial = float(input('Depósitio inicial: R$ '))
taxa_juros = float(input('Taxa de juros (%): '))

mês = 1

while mês <= 12:
    deposito_mensal = float(input('Depósito mensal: R$'))

    depósito_inicial = (depósito_inicial * (1 + (taxa_juros / 100))) + (deposito_mensal)    

    print(f'Mês {mês}: R$ {depósito_inicial:.2f}\n')
    mês = mês + 1

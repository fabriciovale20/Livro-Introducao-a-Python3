"""
    Exercício 10

    Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento.
Exiba o valor do aumento e do novo salário.
"""

salário = float(input('Salário: R$ '))
aumento_porcentagem = float(input('Porcentagem (%) do aumento: '))

salário_atual = salário * (1 +(aumento_porcentagem / 100))

print(f'Salário inicial: R$ {salário:.2f}')
print(f'Aumento: {aumento_porcentagem:.1f}%')
print(f'Salário final: R$ {salário_atual:.2f}')

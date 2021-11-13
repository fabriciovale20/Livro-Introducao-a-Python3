"""
    Exercício 06

    Modifique o Programa 2, de forma que ele calcule um aumento de 15% para um salário de R$750.
"""

salario = 750
aumento = 0.15 # Equivale a 15% (15 / 100) = 0,15

print(f'Salário de R$ {salario:.2f} com auemnto de 15%, ficou R$ {salario + (salario * aumento):.2f}')
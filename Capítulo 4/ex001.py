"""
    Exercício 01

    Analise o programa a seguir e responda o que acontece se o primeiro e o segundo valores forem iguais? Explique
"""

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))

if a > b:
    print('O primeiro valor é o maior!')
if b > a:
    print('O segundo valor é o maior!')

# O programa executará, porém não irá apresentar nenhum retorno, pois não foi inserido um condição para caso os valores de a e b fosse iguais.
# Há apenas duas condições, se a > b e b > a, precisará ter a condição se a == b.

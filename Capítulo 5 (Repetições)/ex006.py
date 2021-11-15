"""
    Exercício 06

    Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2, 2x2 = 4...
"""

número = int(input('Tabuada de: '))
contagem = 1

while contagem <= 10:
    print(f'{número} x {contagem} = {número * contagem}')
    contagem = contagem + 1

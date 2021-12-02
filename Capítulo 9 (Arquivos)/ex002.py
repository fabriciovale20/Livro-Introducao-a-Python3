"""
    Exercício 02

    Modifique o programa do Exercício 9.1 para que receba mais dois parâmetros: a linha de início e a de fim para impressão.
O programa deve imprimir apenas as linhas entre dois valores (incluindo as linhas de início e fim).
"""

nome = input('Digite o nome do arquivo: ')

with open(f'{nome}.txt', 'w') as arquivo:
    for linha in range(1, 101, 2):
        arquivo.write(f'{linha}\n')

with open(f'{nome}.txt', 'r') as arquivo:
    for linha in arquivo.readlines():
        print(linha)

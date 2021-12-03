"""
    Exercício 04

    Crie um programa que receba o nome de dois arquivos como parâmetros da linha de comando e que gere um arquivo de saída com as linhas do
primeiro e do segundo arquivo.
"""

primeiro_arquivo = input('Nome do 1º arquivo: ')
segundo_arquivo = input('Nome do 2º arquivo: ')

with open(f'{primeiro_arquivo}.txt', 'w'):
    with open(f'{segundo_arquivo}.txt', 'w'):
        print()

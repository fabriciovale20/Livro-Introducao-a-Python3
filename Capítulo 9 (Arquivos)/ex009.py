"""
    Exercício 09

    Crie um programa que receba uma lista de nomes de arquivo os imprima, um por um.
"""

while True:
    arquivo = input('Nome do arquivo: ')

    if arquivo == '':
        print('Programa finalizado')
        break
    else:
        with open(f'{arquivo}.txt') as arq:
            for c in arq:
                print(c)

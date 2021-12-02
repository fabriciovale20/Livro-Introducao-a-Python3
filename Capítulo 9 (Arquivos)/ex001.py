"""
    Exercício 01

    Escreva um programa que receba o nome de um arquivo pela linha de comando e que imprima todas as linhas desse arquivo.
"""

nome = input('Digite o nome do arquivo: ')

with open(f'{nome}.txt', 'w') as arquivo:
    for linha in range(1, 101, 2):
        arquivo.write(f'{linha}\n')

with open(f'{nome}.txt', 'r') as arquivo:
    for linha in arquivo.readlines():
        print(linha)

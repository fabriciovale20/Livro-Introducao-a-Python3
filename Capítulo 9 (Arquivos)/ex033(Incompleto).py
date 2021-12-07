"""
    Exercício 33

    Crie um programa que gere uma página uma página html com links para todos os arquivos jpg e png encontrados a partir de um diretório informado
na linha de comando.
"""

import os.path

arquivo = input('Nome do arquivo: ')

if os.path.exists(arquivo):
    print(f'O arquivo "{arquivo}" existe é um ', end='')
    if os.path.isdir(arquivo):
        print('diretório.')
    elif os.path.isfile(arquivo):
        print('arquivo.')
else:
    print(f'O arquivo informado "{arquivo}" não existe.')

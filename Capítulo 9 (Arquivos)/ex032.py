"""
    Exercício 32

    Modifique o Programa 9.9 de forma a receber o nome do arquivo ou diretório a verificar pela linha de comando.
Imprima se existir e se for um arquivo ou um diretório.
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

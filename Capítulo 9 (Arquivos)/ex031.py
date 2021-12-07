"""
    Exercício 31

    Crie um programa que corrija o Programa 9.9 de forma a verificar se z existe e é um diretório.
"""

import os.path

if os.path.exists('z'):
    if os.path.isdir('z'):
     print('O diretório z existe.')
else:
    print('O diretório z não existe.')

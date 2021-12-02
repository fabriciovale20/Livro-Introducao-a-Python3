"""
    Programa 9.2 - Uso do with
"""

import sys

print(f'Número de parâmetros: {len(sys.argv)}')

for n, p in enumerate(sys.argv):
    print(f'Parâmentro {n} = {p}')
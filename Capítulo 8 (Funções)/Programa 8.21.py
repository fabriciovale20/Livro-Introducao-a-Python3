"""
    Programa 8.21 - Navageando listas a partir do tipo de seus elementos
"""

import types

L = ['a', ['b', 'c', 'd'], 'e']

for x in L:
    if isinstance(type(x), str):
        print(x)
    else:
        print('Lista: ')
        for z in x:
            print(z)
            
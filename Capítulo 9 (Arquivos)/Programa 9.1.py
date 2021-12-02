"""
    Programa 9.1 - Abrindo, lend e fechand um arquivo
"""

arquivo = open('números.txt', 'r')

for linha in arquivo.readlines():
    print(linha)

arquivo.close()
"""
    Programa 9.0 - Criando um arquivo
"""

arquivo = open('números.txt', 'w')

for linha in range(1, 101):
    arquivo.write(f'{linha}\n')

arquivo.close()
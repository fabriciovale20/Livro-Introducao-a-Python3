"""
    Programa 9.2 - Uso do with
"""

with open('números.txt', 'r') as arquivo: # Utilizamos o with para fechar o arquivo sem precisar da comando close()

    for linha in arquivo.readlines():
        print(linha)
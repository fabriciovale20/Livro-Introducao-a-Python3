"""
    Exercício 10

    Crie um programa que receba uma lista de nomes de arquivo e que gere apenas um grande arquivo de saída.
"""

lista_nome_arquivos = []

while True:
    arquivo = input('Nome do arquivo: ')

    if arquivo == '':
        break
    else:
        lista_nome_arquivos.append(arquivo)

with open('grande_arquivo.txt', 'w') as arquivo_grande:
    for c in lista_nome_arquivos:
        print(c)
        with open(f'{c}.txt') as arq:
            for n in arq.readlines():
                arquivo_grande.write(n)

"""
    Exercício 13

    Crie um programa que imprima as linhas de um arquivo. Esse programa deve receber três parâmetros pela linha de comando: o nome do arquivo,
a linha inicial e a última linha a imprimir.
"""
linha = 0

nome_arquivo = input('Nomo do arquivo: ')

with open(f'{nome_arquivo}.txt') as arquivo:
    inicio = int(input('Linha inicial: '))
    fim = int(input('Linha final: '))

    for c in arquivo:
        c = c.replace('\n','')
        if linha >= inicio and linha < fim:
            print(c)
        elif linha == fim:
            print(c)
            break

        linha += 1
        


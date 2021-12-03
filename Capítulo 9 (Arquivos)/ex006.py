"""
    Exercício 06

    Modifique o Programa 9.5 para imprimir 40 vezes o símbolo de = se este for o primeiro caractere da linha. Adicione também a opção para parar
de imprimir até que se pressione a tecla Enter cada vez que uma linha iniciar com . (ponto) como primeiro caractere.
"""

LARGURA = 79

with open('entradaex006.txt') as entrada:
    for linha in entrada.readlines():
        if linha[0] == ';':
            continue
        elif linha[0] == '>':
            print(linha[1:].rjust(LARGURA))
        elif linha[0] == '*':
            print(linha[1:].center(LARGURA))
        elif linha[0] == '=':
            print('='*40)
        elif linha[0] == '.':
            n = input('Digite enter para continuar: ')
        else:
            print(linha)

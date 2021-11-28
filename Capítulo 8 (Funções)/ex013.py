"""
    Exercício 13

    Escreva uma função que receba uma string com as opões válidas a acertar (cada opção é uma letra). Converta as opções válidas para letras
minúsculas. Utilze input para ler uma opção, converter o valor para letras minúsculas e verificar se a opção é válida. Em caso de opção inválida,
a função deve pedir ao usuário que digite novamente outra opção.
"""

def validar(string):
    opções_válidas = ['a', 'b', 'c', 'd']
    return True if string in opções_válidas else False

while True:
    opção = input('''\nEscolha uma das opções abaixo:
a) Nome;
b) Idade;
c) CPF;
d) Cidade

Qual sua opção: ''').lower().strip()
    
    if validar(opção):
        print('\033[1;92mOpção válida\033[m')
        break
    else:
        print('\033[1;91mOpção inválida, tente novamente\033[m')
    

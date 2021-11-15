"""
    Exercício 03

    Faça um programa para escreva a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8..., 1, 0 e Fogo! na tela.
"""

contagem = 10

while contagem >= 0:
    print(contagem, end=' ')
    contagem = contagem - 1

print('Fogo!')

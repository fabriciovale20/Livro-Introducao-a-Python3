"""
    Exercício 14

    Altere o Programa 8.20 de forma que o usuário tenha três chances de acertar o número.
O programa termina se o usuário acertar ou errar três vezes.
"""

import random

n = random.randint(1, 10)

tentativas = 1

while tentativas <= 3:
    x = int(input('Escolha um número entre 1 e 10: '))

    if x == n:
        print('Você acertou!')
        break
    else:
        print('Você errou.')
        tentativas += 1

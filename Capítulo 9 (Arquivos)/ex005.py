"""
    Exercício 05

    Crie um programa que inverta a ordem das linhas do arquivo pares.txt. A primeira linha deve conter o maior número; e a última, o menor.
"""

números = []

with open('paresex05.txt', 'w') as paresex05:
    with open('pares.txt') as pares:
        for n in pares:
            números.append(int(n))

        números = sorted(números, reverse=True)

        for n in números:
            paresex05.write(f'{str(n)}\n')

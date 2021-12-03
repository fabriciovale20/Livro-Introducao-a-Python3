"""
    Exercício 03

    Crie um programa que lia os arquivos pares.txt e impares.txt e que crie um só arquivo paresimpares.txt com todas as linhas dos
outros dois arquivos, de forma a preservar a ordem numérica.
"""

números = []

with open('paresimpares.txt', 'w') as paresimpares:
    with open('pares.txt') as pares:
        with open('ímpares.txt') as ímpares:
            for n in pares:
                números.append(int(n))
            for n in ímpares:
                números.append(int(n))
            
            números = sorted(números)
            
            for n in números:
                paresimpares.write(f'{str(n)}\n')

"""
    Programa 9.4 - With em uma só linha
"""

with open('ímpares.txt', 'w') as ímpares, open('pares.txt', 'w') as pares:
    for n in range(0, 1000):
        if n % 2 == 0:
            pares.write(f'{n}\n')
        else:
            ímpares.write(f'{n}\n')

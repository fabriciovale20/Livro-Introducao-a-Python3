"""
    Exercício 17

    Escreva um generator capaz de gerar a série dos números primos.
"""

cont = 0

for c in range(100):
    for x in c:
        if c % x == 0:
            cont += 1

    if cont == 2:
        print(f'{c} é primo')
        
    cont = 0

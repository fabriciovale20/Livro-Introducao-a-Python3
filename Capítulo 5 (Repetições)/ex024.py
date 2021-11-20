"""
    Exercício 24

    Modifique o programa anterior de forma a ler um número n.
Imprima os n primeiros números primos.
"""

número = int(input('Digite um valor: '))

cont = 0

print('Números primos: ', end='')

while número > cont:
    cont += 1
    n = primo = 0

    while cont > n:
        n += 1

        if cont % n == 0:
            primo += 1


    if primo == 2:
        print(cont, end=' ')

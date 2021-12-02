"""
    Exercício 17

    Escreva um generator capaz de gerar a série dos números primos.
"""

termos = 100

def primo():
    for n in range(1, termos):
        primo = 0

        for c in range(1, n+1):
            if n % c == 0:
                primo += 1

        if primo == 2:
            yield n

print([x for x in primo()])
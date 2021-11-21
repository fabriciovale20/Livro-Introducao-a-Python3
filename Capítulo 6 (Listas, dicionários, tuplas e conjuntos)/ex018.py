"""
    Exercício 18

    Escreva um programa que gere um dicionário, em que cada chave seja um caractere, e seu valor seja o número
desse caractere encontrado em uma frase lida.
Exemplo: O rato → {'O':1, ' ':1, 'r':1, 'a':1, 't':1, 'o':1}
"""

frase = {'O':1, ' ':1, 'r':1, 'a':1, 't':1, 'o':1}

for chave, dado in frase.items():
    print(f'{chave}', end='')

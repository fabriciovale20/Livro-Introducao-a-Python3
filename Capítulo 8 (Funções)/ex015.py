"""
    Exercício 15


"""

import random

n = random.randint(0, 4)
lista = ['python', 'programação', 'exercícios', 'livro', 'computador']

palavra = lista[n]

for x in range(100):
    print()

digitadas = []
acertos = []
erros = 0

while True:
    senha = ''

    for letra in palavra:
        senha += letra if letra in acertos else '.' # 3
    print(senha)

    if senha == palavra:
        print('Você acertou!')
        break

    tentativa = input('\nDigite uma letra: ').lower().strip()

    if tentativa in digitadas:
        print('Você já tentou essa letra!')
        continue # 4
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print('Você errou!')
    print('X==:==\nX  :  ')
    print('X  O  ' if erros >= 1 else 'X')
    linha2 = ''

    if erros == 2:
        linha2 = '  |  '
    elif erros == 3:
        linha2 = ' \|  '
    elif erros >= 4:
        linha2 = ' \|/ '

    print(f'X{linha2}')
    linha3 = ''

    if erros == 5:
        linha3 += ' /  '
    elif erros >= 6:
        linha3 += ' / \ '
    print(f'X{linha3}')
    print('X\n-----------')
    if erros == 6:
        print('Enforcado!')
        break


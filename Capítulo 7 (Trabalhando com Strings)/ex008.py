"""
    Exercício 08

    Modifique o Programa 7.2 de forma a utilizar uma lista da palavras.
No início, pergunte um número e calcule o índice da palavra a utilizar pela fórmula: indice = (número * 776) % len(lista_de_palavras)
"""

palavra = input('Digite a palavra secreta: ').lower().strip() # 1

lista_de_palavras = [palavra]
número = int(input('Digite um número: '))
indice = (número * 776) % len(lista_de_palavras)

for x in range(100):
    print() # 2

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
        linha2 = ' /|  '
    elif erros >= 4:
        linha2 = ' /|\ '

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
        print(f'A palavra secreta é: {palavra}')
        break


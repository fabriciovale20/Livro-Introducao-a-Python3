"""
    Exercício 09

    Modifique o Programa 7.2 para utilizar listas de strings para desenhar o boneco da forca. Você pode utilizar uma lista para cada linha
e organizá-las em uma lista de listas. Em vez de controlar quando imprimir cada parte, desenhe nestas listas, substituindo o elemento a desenhar:
Exemplo:
linha = list('X------')
linha
['X', '-', '-', '-', '-', '-', '-']

linha[6] = '|'
linha
['X', '-', '-', '-', '-', '-', '|']
''.join(linha)
'X-----|'
"""

palavra = input('Digite a palavra secreta: ').lower().strip() # 1

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
    
    linha = list('      ')

    if erros == 2:
        linha[2] = '|'
    elif erros == 3:
        linha[1] = '/'
        linha[2] = '|'
    elif erros >= 4:
        linha[1] = '/'
        linha[2] = '|'
        linha[3] = '\\'

    linha = ''.join(linha)
    print(f'X{linha}')

    linha3 = list('      ')

    if erros == 5:
        linha3[1] = '/'
    elif erros >= 6:
        linha3[1] = '/'
        linha3[3] = '\\'
    
    linha3 = ''.join(linha3)
    print(f'X{linha3}')

    print('X\n-----------')
    if erros == 6:
        print('Enforcado!')
        print(f'A palavra secreta é: {palavra}')
        break


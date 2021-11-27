"""
    Exercício 10

    Escreva um jogo da velha para dois jogadores. O jogo deve perguntar onde você quer jogar e alternar entre os jogadores.
A cada jogada, verifique se a posição está livre. Verifique também quando um jogador venceu a partida. Um jogo da velha pode ser visto
como uma lista de 3 elementos, na qual cada elemento é outra lista, também com três elementos.
Exemplo do jogo:
 X | O |   
---+---+---
   | X | X 
---+---+---
   |   | O 

Em que cada posição pode ser vista como um número. Confira a seguir um exemplo das posições mapeadas para a mesma posição de seu teclado numérico.
 7 | 8 | 9 
---+---+---
 4 | 5 | 6 
---+---+---
 1 | 2 | 3 
"""

print('Jogo da Velha')
print('Escolha um número de 1 à 9 para preencher o espaço escolhido')

opções = [1, 2, 3, 4, 5, 6, 7, 8, 9]
linha1 = list('   |   |   ')
linha2 = list('   |   |   ')
linha3 = list('   |   |   ')
linha_divisão = list('---+---+---')

print(''.join(linha1))
print(''.join(linha_divisão))
print(''.join(linha2))
print(''.join(linha_divisão))
print(''.join(linha3))
print()

cont = 1    
jogador = 1
caractere = ''
registro_jogadas = []

# Utilizado valor 1 e -1 para lógica do ganhado, se em algum momento somar 3 ou -3 em alguma linha ou diagonal, há um vencedor.
vencer = [[], [], [], [], []]
jogador_1 = []
jogador_2 = []

while cont <= 9:
    if cont % 2 != 0:
        jogador = 1
        caractere = 'X'
        valor = 1
    else:
        jogador = 2
        caractere = 'O'
        valor = -1

    while True:
        jogada_x_o = int(input('Jogador 1, sua jogada: '))

        if jogada_x_o not in opções:
            print('Jogada inválida, tente novamente!')
            continue

        if jogada_x_o in registro_jogadas:
            print('Jogada já escolhida, escolha outra jogada.')
            continue

        # Linha de cima
        elif jogada_x_o == 7:
            linha1[1] = caractere
            vencer[2].append(valor)
            vencer[3].append(valor)
        elif jogada_x_o == 8:
            linha1[5] = caractere
            vencer[2].append(valor)
        elif jogada_x_o == 9:
            linha1[9] = caractere
            vencer[2].append(valor)
            vencer[4].append(valor)


        # Linha do meio
        elif jogada_x_o == 4:
            linha2[1] = caractere
            vencer[1].append(valor)
        elif jogada_x_o == 5:
            linha2[5] = caractere
            vencer[1].append(valor)
            vencer[3].append(valor)
            vencer[4].append(valor)
        elif jogada_x_o == 6:
            linha2[9] = caractere
            vencer[1].append(valor)

        # Linha de baixo
        elif jogada_x_o == 1:
            linha3[1] = caractere
            vencer[0].append(valor)
            vencer[4].append(valor)
        elif jogada_x_o == 2:
            linha3[5] = caractere
            vencer[0].append(valor)
        elif jogada_x_o == 3:
            linha3[9] = caractere
            vencer[0].append(valor)
            vencer[3].append(valor)

        registro_jogadas.append(jogada_x_o)     

        print(''.join(linha1))
        print(''.join(linha_divisão))
        print(''.join(linha2))
        print(''.join(linha_divisão))
        print(''.join(linha3))

        # Realizar a verificar se algum jogar venceu
        for i, v in enumerate(vencer):
            if sum(v) == 3:
                print('-'*20)
                print('O jogador 1 venceu!')
                cont = 10
            elif sum(v) == -3:
                print('-'*20)
                print('O jogador 2 venceu!')
                cont = 10

        break


    cont += 1

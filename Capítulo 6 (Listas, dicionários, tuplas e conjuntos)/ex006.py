"""
    Exercício 06

    Modifique o programa para trabalhar com duas filas. Para facilitar seu trabalho, considere o comando A para atendimento da fila;
e B, para atendimento da fila 2. O mesmo para a chegada de clientes: F para fila 1; e G, para fila 2.
"""

último_1 = int(input('Fila 1: '))
último_2 = int(input('Fila 2: '))

fila_1 = list(range(1, último_1 + 1))
fila_2 = list(range(1, último_2 + 1))

while True:
    print(f'\nFila 1: {fila_1}')
    print(f'Fila 2: {fila_2}')
    print('Digite A (Fila 1) e B (Fila 2) para atendimento, F (Fila 1) e G (Fila 2) para adicionar')

    operação = input('Operações (A/B, F/G ou S): ')

    if operação in 'AB':
        if operação == 'A':
            if len(fila_1) > 0:
                atendido = fila_1.pop(0)
                print(f'\033[97mCliente {atendido} atendido (Fila 1).\033[m')
            else:
                print('\033[91mFila 1 vazia! Ninguém para atender.\033[m')
        else:
            if len(fila_2) > 0:
                atendido = fila_2.pop(0)
                print(f'\033[97mCliente {atendido} atendido (Fila 2).\033[m')
            else:
                print('\033[91mFila 2 vazia! Ninguém para atender.\033[m')

    elif operação in 'FG':
        if operação == 'F':
            último_1 += 1 
            fila_1.append(último_1)
        else:
            último_2 += 1
            fila_2.append(último_2)

    elif operação == 'S':
        print('Programa finalizado!')
        break
    else:
        print('Operação inválida! Digite apenas A/B, F/G ou S!')
    
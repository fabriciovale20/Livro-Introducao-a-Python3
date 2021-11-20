"""
    Exercício 05

    Altere o programa 6.7 de forma a poder trabalhar com vários comandos digitados de uma só vez. Atualmente, apenas um comando pode
ser inserido por vez. Altere-o de forma a considerar operação como uma string.

Exemplo: FFFAAAS significaria três chegadas de novos clientes, três atendimentos e, finalmente, a saída do programa.
"""

último = 10
fila = list(range(1, último + 1))

while True:
    print(f'\nExistem {len(fila)} clientes na fila')
    print(f'Fila atual: {fila}')
    print('Digite F para adicionar um cliente ao fim da fila,')
    print('ou A para realizar o atendimento. S para sair.')

    sequencia = []

    while True:
        opc = input('Operações (F, A ou S): ')
        sequencia.append(opc)

        if opc == 'S':
            break

    while len(sequencia) > 0:
        operação = sequencia[0]

        if operação == 'A':
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f'Cliente {atendido} atendido')
            else:
                print('Fila vazia! Ninguém para atender.')
        elif operação == 'F':
            último += 1 # Incrementa o ticket do novo cliente
            fila.append(último)
        elif operação == 'S':
            break
        else:
            print('Operação inválida! Digite apenas F, A ou S!')
        
        del sequencia[0]

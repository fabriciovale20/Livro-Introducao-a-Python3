"""
    Exercício 04

    O que acontece quando não verificamos se a lista está vazia antes de chamarmos o método pop?
    Resposta: Não irá acontecer nada, apenas a lista estará vazia.
"""

último = 0
fila = list(range(1, último + 1))

while True:
    print(f'\nExistem {len(fila)} clientes na fila')
    print(f'Fila atual: {fila}')
    print('Digite F para adicionar um cliente ao fim da fila,')
    print('ou A para realizar o atendimento. S para sair.')

    operação = input('Operação (F, A ou S): ')

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

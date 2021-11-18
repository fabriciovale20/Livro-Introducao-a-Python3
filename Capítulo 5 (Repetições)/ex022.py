"""
    Exercício 22

    Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair.
Imprima a tabuada da operação escolhida. Repita até que a opção saída seja escolhida.
"""

a = int(input('Número: '))

while True:
    print('''Lista de Opções
1- Adição
2- Subtração
3- Divisão
4- Multiplicação
5- Sair''')

    opção = int(input('Escolha sua opção: '))

    while opção < 1 or opção > 5:
        print('Opção inválida, tente novamente.')
        opção = int(input('Escolha sua opção: '))

    if opção == 5:
        print('Programa finalizado')
        break
    
    tabuada = 1

    if opção == 1:
        while tabuada <= 10:
            print(f'{a} + {tabuada} = {a + tabuada}')
            tabuada += 1
    elif opção == 2:
        while tabuada <= 10:
            print(f'{a} - {tabuada} = {a - tabuada}')
            tabuada += 1
    elif opção == 3:
        while tabuada <= 10:
            print(f'{a} ÷ {tabuada} = {a / tabuada}')
            tabuada += 1
    else:
        while tabuada <= 10:
            print(f'{a} x {tabuada} = {a * tabuada}')
            tabuada += 1

    print()
    
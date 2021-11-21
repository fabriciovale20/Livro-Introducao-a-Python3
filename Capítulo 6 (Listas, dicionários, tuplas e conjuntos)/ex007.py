"""
    Exercício 07

    Faça um programa que leia uma expressão com parênteses. Usando pilhas, verifique se os parênteses foram abertos e fechados na ordem correta.
Exemplo:
(())       OK
()()(()()) OK
())        ERRO
"""

expressão = input('Digite a expressão: ')
cont = 0
lista = []

while cont < len(expressão):
    if expressão[cont] == '(':
        lista.append(expressão[cont])
    elif expressão[cont] == ')':
        if len(lista) > 0:
            lista.pop(-1)
        else:
            lista.append(')')
            break

    cont += 1

print(lista)
if len(lista) != 0:
    print('Expressão inválida.')
else:
    print('Expressão válida.')

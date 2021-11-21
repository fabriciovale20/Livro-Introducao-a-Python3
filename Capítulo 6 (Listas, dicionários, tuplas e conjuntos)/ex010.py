"""
    Exercício 10

    Modifique o programa do Exercício 6.9 de forma a pesquisar p e v em toda a lista
e informando ao usuário a posição onde p e a posição onde v foram encontrados.
"""

L = [15, 7, 27, 39]
p = int(input('Digite o primeiro valor a procurar: '))
v = int(input('Digite o segundo valor a procurar: '))

pos_p = 0

# Buscando o primeiro valor
while pos_p < len(L):
    if L[pos_p] == p:
        print(f'{p} achado na posição {pos_p}')
        break
    elif pos_p == len(L)-1:
        print(f'{p} não encontrado')
        pos_p = 'n'
        break

    pos_p += 1

pos_v = 0
# Buscando o segundo valor
while pos_v < len(L):
    if L[pos_v] == v:
        print(f'{v} achado na posição {pos_v}')
        break
    elif pos_v == len(L)-1:
        print(f'{v} não encontrado')
        pos_v = 'n'
        break

    pos_v += 1

print()
if type(pos_p) == int and type(pos_v) == int:
    if pos_p > pos_v:
        print(f'O segundo valor {v} foi encontrado primeiro ({p} na posição {pos_p} e {v} na posição {pos_v}).')
    elif pos_p < pos_v:
        print(f'O primeiro valor {p} foi encontrado primeiro ({p} na posição {pos_p} e {v} na posição {pos_v}).')
    else:
        print(f'Os dois valores são iguais, foram encontrados ao mesmo tempo (Posição {pos_p}).')

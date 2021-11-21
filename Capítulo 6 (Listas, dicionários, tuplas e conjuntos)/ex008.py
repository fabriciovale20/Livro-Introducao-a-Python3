"""
    Exercício 08

    Modifique o primeiro exemplo (Programa 6.9) de forma a realizar a mesma tarefa, mas sem utilizar a variável achou.
Dica: observe a condição de saída do while.
"""

L = [15, 7, 27, 39]
p = int(input('Digite o valor a procurar: '))

x = 0

while x < len(L):
    if L[x] == p:
        print(f'{p} achado na posição {x}')
        break
    elif x == len(L)-1:
        print(f'{p} não encontrado')
        break

    x += 1

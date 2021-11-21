"""
    Exercício 15

    O que acontece quando dois valores são iguais? Rastreie o Programa 6.20, mas com a lista L = [3, 3, 1, 5, 4]

Resposta: Executa o programa normalmente, mas não precisará realizar a troca entre os dois números iguais. Pois a condição só executará se for maior.
"""

L = [3, 3, 1, 5, 4]
fim = 5

while fim > 1:
    trocou = False
    x = 0

    while x < (fim - 1):
        if L[x] > L[x + 1]:
            trocou = True
            temp = L[x]
            L[x] = L[x + 1]
            L[x + 1] = temp
            
        x += 1

    if not trocou:
        break

    fim -= 1

for e in L:
    print(e)

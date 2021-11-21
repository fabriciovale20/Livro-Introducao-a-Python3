"""
    Exercício 11

    Modifique o Programa 6.6 usando for. Explique por que nem todos os while podem ser transformados em for.
    
Resposta: Não temos como inserir o FOR, pois não sabemos quantas vezes haverá interação do usuário ao programa, não sabemos quando
o usuário irá encerrar o programa.
"""

L = []

while True:
    n = int(input('Digite um número (0 sai): '))

    if n == 0:
        break
    L.append(n)

x = 0

while x < len(L):
    print(L[x])
    x += 1

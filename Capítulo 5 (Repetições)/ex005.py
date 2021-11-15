"""
    Exercício 05

    Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3.
"""

contagem = 1
número = 1

while contagem <= 10:
    if número % 3 == 0:
        print(número)
        contagem = contagem + 1
        
    número = número + 1

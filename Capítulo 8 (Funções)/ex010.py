"""
    Exercício 10

    Reescreva a função para cálculo de sequência de Fibonacci, sem utilizar a recursão.
"""

from time import sleep

def fibonacci(termos):
    n = 0
    p_anterior = 1
    s_anterior = 0
    cont = 1

    while termos >= cont:
        if n <= 0:
            print(n)
            s_anterior = p_anterior
            p_anterior = n
            n += 1
            
        else:
            n = p_anterior + s_anterior
            s_anterior = p_anterior
            p_anterior = n
            sleep(1)
            print(n)
        
        cont += 1

fibonacci(10)
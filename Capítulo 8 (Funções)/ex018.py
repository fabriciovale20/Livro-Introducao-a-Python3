"""
    Exercício 18

    Escreva um generator capaz de gerar a série de Fibonacci.
"""

def fibonacci():
    p = 0
    s = 1
    
    while s < 100:
        
        yield s
        p, s = s, s + p

print([x for x in fibonacci()])

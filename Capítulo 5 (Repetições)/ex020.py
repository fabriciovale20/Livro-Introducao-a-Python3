"""
    Exercício 20

    O que acontece se digitarmos 0,001 no programa anterior? Caso ele não funcione, altere o de forma a corrigir o problema.
"""

valor = float(input('Digite o valor a pagar: '))
cédulas = 0
atual = 100
apagar = valor

while True:
    if atual <= apagar:
        apagar -= atual
        cédulas += 1
    else:
        print(f'{cédulas} cédula(s) de R$ {atual}')
        if apagar == 0:
            break
        
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        elif atual == 1:
            atual = 0.5
        elif atual == 0.5:
            atual = 0.1
        elif atual == 0.1:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.02
        elif atual == 0.02:
            atual = 0.01
        elif atual == 0.01:
            atual = 0.001
        cédulas = 0


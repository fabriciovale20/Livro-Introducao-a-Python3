"""
    Exercício 14

    Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado pelo usuário,
assim como a quantidade de dias pelos quais o carro foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""

km_percorrido = float(input('Distância percorrida (Km): '))
dias = int(input('Dias alugados: '))

valor_a_pagar = (dias * 60) + (km_percorrido * 0.15)

print(f'O usuário terá que pagar R$ {valor_a_pagar:.2f}.')

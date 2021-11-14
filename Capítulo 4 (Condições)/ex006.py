"""
    Exercício 06

    Escreva um programa que pergunte a distância que um passageiro deseja percorrer em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até de 200Km, e R$0,45 para viagens mais longas.
"""

distância = int(input('Distância percorrida (Km): '))

if distância <= 200:
    preço = 'R$ 0,50'
    valor = distância * 0.5
else:
    preço = 'R$ 0,45'
    valor = distância * 0.45

print(f'Distância percorrida de {distância} Km, taxa de {preço}, total à pagar R$ {valor:.2f}.')

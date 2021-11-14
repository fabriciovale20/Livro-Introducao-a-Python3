"""
    Exercício 12

    Faça um programa que calcule o tempo de uma viagem de carro.
Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
"""

distância = float(input('Distância à percorrer (Km): '))
velocidade_média = float(input('Velocidade média (Km/h): '))

tempo = (distância / velocidade_média)

print(f'Numa distância de {distância} Km à uma velocidade média de {velocidade_média} Km/h, você chegará ao destino em {tempo:.2f} horas.')

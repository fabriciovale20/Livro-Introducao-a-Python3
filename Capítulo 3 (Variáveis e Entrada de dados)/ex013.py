"""
    Exercício 13

    Escreva um programa que converta uma temperatua digitada em ºC em ºF. A fórmula para essa conversão é F = ((9 x C) / 5) + 32
"""

temperatura_celsius = float(input('Temperatura em ºC: '))

temperatura_fahrenheit = ((9 * temperatura_celsius) / 5) + 32

print(f'Temperatura em Fahrenheit {temperatura_fahrenheit:.2f} ºF.')

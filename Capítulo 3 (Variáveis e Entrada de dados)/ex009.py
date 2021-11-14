"""
    Exercício 09

    Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.    
"""

print('Informe a quantidade de...')
dias = int(input('Dias: '))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))

total_segundos_dias = (dias*24*60*60)
total_segundos_horas = (horas*60*60)
total_segundos_minutos = (minutos*60)
total_soma = total_segundos_dias + total_segundos_horas + total_segundos_minutos

print(f'{dias} dias tem {total_segundos_dias} segundos.')
print(f'{horas} dias tem {total_segundos_horas} segundos.')
print(f'{minutos} dias tem {total_segundos_minutos} segundos.')

print(f'\nTotal de {total_soma} segundos.')

"""
    Exercício 13

    A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T = [-10, -8, 0, 1, 2, 5, -2, -4].
Faça um programa que imprima a menor e a maior temperatura, assim como a temperatura média.
"""

T = [-10, -8, 0, 1, 2, 5, -2, -4]
maior = menor = T[0]
soma_temperatura = 0

for temperatura in T:
    if temperatura > maior:
        maior = temperatura
    
    if temperatura < menor:
        menor = temperatura

    soma_temperatura += temperatura

print(f'''{' COLETA DE TEMPERATURAS ':-^30}
Maior: {maior}
Menor: {menor}
Média: {soma_temperatura / len(T)}''')

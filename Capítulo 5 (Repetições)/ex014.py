"""
    Exercício 14

    Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução,
exiba a quantidade de números digitados, assim como a soma e a média aritmética.
"""

soma = números_digitados = 0

while True:
    valor = int(input('Digite um valor: '))

    if valor == 0:
        break

    soma += valor
    números_digitados += 1

print(f'''\nQuantidade de números digitados: {números_digitados}
Soma dos números: {soma}
Média aritmética: {soma/números_digitados}
''')

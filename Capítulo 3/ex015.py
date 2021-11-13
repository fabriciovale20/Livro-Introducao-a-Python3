"""
    Exercício 15

    Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos ela já fumou.
Considere que um fumante perde 10 minutos de vida a cada cigarro e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
"""

quantidade_cigarros_por_dia = int(input('Quantidade de cigarros fumados por dia: '))
quantidade_cigarros_fumado = int(input('Quantos cigarros você já fumou? '))

tempo_perdido_por_dia = (quantidade_cigarros_por_dia * 10)
tempo_já_perdido = (quantidade_cigarros_fumado * 10)

tempo_em_dias = ((tempo_perdido_por_dia + tempo_já_perdido) / 60 ) / 24

print(f'Você perde cerca de {tempo_perdido_por_dia} minutos de vida por dia.')
print(f'Você já perdeu {tempo_já_perdido} minutos de vida pelos cigarros fumados.')
print(f'Totalizando {tempo_em_dias:.0f} dias perdidos.')


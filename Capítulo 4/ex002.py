"""
    Exercício 02

    Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h,
exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$5 por km acima de 80 km/h. 
"""

velocidade_do_carro = float(input('Velocidade do carro: '))

if velocidade_do_carro > 80:
    multa = (velocidade_do_carro - 80) * 5
    print(f'Velocidade acima do permitido, você foi multado em R$ {multa:.2f}')

if velocidade_do_carro <= 80:
    print('Velocidade permitida, boa viagem.')
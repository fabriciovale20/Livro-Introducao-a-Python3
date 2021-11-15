"""
    Exercício 07

    Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada, em vez de começar com 1 e 10.
"""

número = int(input('Tabuada de: '))
início = int(input('Início: '))
fim = int(input('Fim: '))

# Quando o INÍCIO for MENOR que o FIM.
if fim > início:
    while início <= fim:
        print(f'{número} x {início} = {número * início}')
        início = início + 1

# Quando o INÍCIO for MAIOR que o FIM.
elif fim < início:
    while início >= fim:
        print(f'{número} x {início} = {número * início}')
        início = início - 1

# Quando o INÍCIO e FIM forem IGUAIS.
else:
    print(f'{número} x {início} = {número * início}')
"""
    Exercício 15

    Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto
e a quantidade comprada. Utilize a tabela de código a seguir para obter o preço de cada produto:

Código  Preço
  1      0,50  
  2      1,00
  3      4,00
  4      7,00
  9      8,00

Seu programa deve exibir o total das compras depois que o usuáro digitar 0. Qualquer outro código deve gerar a mensagem de erro "Código inválido".
"""

soma = 0

while True:
    códig_produto = int(input('Código do produto: '))
    
    if códig_produto == 0:
        print('Compras finalizadas.')
        break
    elif códig_produto >= 5 and códig_produto <= 8 or códig_produto > 9:
        print('Código inválido, tente novamente!')
    else:
        quantidade_comprada = int(input('Quantidade comprada: '))

        if códig_produto == 1:
            soma += quantidade_comprada * 0.5
        elif códig_produto == 2:
            soma += quantidade_comprada * 1
        elif códig_produto == 3:
            soma += quantidade_comprada * 4
        elif códig_produto == 4:
            soma += quantidade_comprada * 7
        else:
            soma += quantidade_comprada * 8

print(f'\nValor total: R$ {soma:.2f}')

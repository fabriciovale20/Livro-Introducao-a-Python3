"""
    Programa 6.19 - Criação e impressão da lista de compras    
"""

produtos = []

while True:
    produto = str(input('\nProduto: '))

    if produto == 'fim':
        break

    quantidade = int(input('Quantidade: '))
    preço = float(input('Preço: R$ '))

    produtos.append([produto, quantidade, preço])

soma = 0

print(f'''\n{' RESUMO COMPRAS ':^20}''')
for prod in produtos:
    print(f'{prod[0]:^6s} - {prod[1]:4d} - R$ {prod[2] * prod[1]:6.2f}')
    soma += prod[1] * prod[2]

print(f'\nTotal compras: R$ {soma:.2f}')

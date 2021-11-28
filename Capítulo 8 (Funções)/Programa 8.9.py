"""
    Programa 8.9 - Validação de inteiro usando função
"""

def faixa_int(pergunta, mínimo, máximo):
    while True:
        v = int(input(pergunta))
        
        if v < mínimo or v > máximo:
            print(f'Valor inválido. Digite um valor entre {mínimo} e {máximo}')
        else:
            return v
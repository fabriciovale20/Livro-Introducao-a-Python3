"""
    Programa 8.11 - Função retângulo com parâmetros obrigatórios e opcionais
"""

def retângulo(largura, altura, caractere='*'):
    linha = caractere * largura
    
    for i in range(altura):
        print(linha)

# Os parâmetros podem ser passados em qualquer ordem
print('Primeira')
retângulo(3, 4)

print('\nSegunda')
retângulo(largura=3, altura=4)

print('\nTerceira')
retângulo(altura=4, largura=3)

print('\nQuarta')
retângulo(caractere='.', altura=4, largura=3)

# Porém precisam seguir a mesma forma de chamada, segue abaixo exemplos INVÁLIDOS de chamadas:
# retângulo(largura=3, 4)
# retângulo(largura=3, altura=4, '*')

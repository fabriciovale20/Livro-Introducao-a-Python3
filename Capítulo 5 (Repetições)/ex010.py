"""
    Exercício 10

    Modifique o programa anterior para que aceite respostas com letras maiúsculas e minúsculas em todas as questões.
"""

pontos = 0
questão = 1

while questão <= 3:
    resposta = input(f'Resposta da questão {questão}: ')

    if questão == 1 and resposta in 'Bb':
        pontos = pontos + 1
    if questão == 2 and resposta in 'Aa':
        pontos = pontos + 1
    if questão == 3 and resposta in 'Dd':
        pontos = pontos + 1
    
    questão = questão + 1

print(f'O aluno fez {pontos} ponto(s).')
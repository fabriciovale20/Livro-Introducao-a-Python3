"""
    Exercício 12

    Modifique o programa do Exercício 9.11 para também registrar a linha e a coluna de cada ocorrência da palavra no arquivo. Para isso, utilize
listas nos valores de cada palavra, guardando a linha e a coluna de cada ocorrência.
"""

lista = ['Ola pessoal']
pal = []

for c in lista:
    palavra = ''
    for n in c:
        if n != ' ':
            palavra += n
            print(palavra)
        else:
            pal.append(palavra)
            palavra = ''
    
    pal.append(palavra)
        
print(pal)
"""
    Exercício 12

    Modifique o programa do Exercício 9.11 para também registrar a linha e a coluna de cada ocorrência da palavra no arquivo. Para isso, utilize
listas nos valores de cada palavra, guardando a linha e a coluna de cada ocorrência.
"""

palavras = {}
lista = []

with open('textoex011.txt') as texto:
    for c in texto:
        palavra = ''

        for n in c:
            n = n.replace('\n', '')

            if n != ' ':
                palavra += n
            else:
                lista.append(palavra)
                palavra = ''
                continue
        
        lista.append(palavra)

    for c in lista:
        if c not in palavras:
            palavras[c] = 1
        else:
            palavras[c] += 1
    
print(palavras)
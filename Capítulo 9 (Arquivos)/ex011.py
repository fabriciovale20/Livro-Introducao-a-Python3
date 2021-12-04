"""
    Exercício 11

    Crie um programa que leia um arquivo e crie um dicionário onde cada chave é uma palavra e cada valor é o número de ocorrências no arquivo.
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
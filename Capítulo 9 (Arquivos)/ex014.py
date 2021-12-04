"""
    Exercício 14

    Crie um programa que leia um arquivo-texto e elimine os espaços repetidos entre as palavras e no fim das linhas. O arquivo de saída também
não deve ter mais de uma linha em branco repetida.
"""
anterior = ''
with open('paginadoex007.txt') as arquivo:
    with open('arquivo_de_saidaex014.txt', 'w') as saida:
        for c in arquivo:
            if len(c) != 1:
                for l in c:
                    if l == ' ':
                        if anterior == l:
                            anterior = l
                            l = l.replace(' ','')
                        else:
                            anterior = l
                    else:
                        anterior = ''
                        
                    saida.write(l)

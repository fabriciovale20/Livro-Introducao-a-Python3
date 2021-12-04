"""
    Exercício 07

    Crie um programa que leia um arquivo-text e gere um arquivo de saída paginado. Cada linha não deve conter mais e 76 caracteres.
Cada página terá no máximo 60 linhas. Adicione na última linha de cada página o número da página atual e o nome do arquivo original.
"""

pagina = linhas = 1

with open('textoex007.txt') as texto:
    with open('paginadoex007.txt', 'w') as pag:
        for palavras in texto.readlines():

            if linhas < 60 and len(palavras[0]) <= 76:
                pag.write(f'{palavras}')
                linhas += 1
            else:
                pag.write(f'Pagina {pagina}\n')
                pagina += 1
                linhas = 1
                    

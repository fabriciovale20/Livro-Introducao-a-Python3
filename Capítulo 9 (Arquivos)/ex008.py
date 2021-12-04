"""
    Exercício 08

    Modifique o programa anterior para também receber o número de caracteres por linha e o número de páginas por filha pela linha de comando.
"""

pagina = linhas = 1

linhas_folhas = int(input('Número de linhas por página? '))
caractere = int(input('Número mínimo de caractere? '))

with open('textoex007.txt') as texto:
    with open('paginadoex008.txt', 'w') as pag:
        for palavras in texto.readlines():

            if linhas < linhas_folhas and len(palavras[0]) <= caractere:
                pag.write(f'{palavras}')
                linhas += 1
            else:
                pag.write(f'Pagina {pagina}\n')
                pagina += 1
                linhas = 1

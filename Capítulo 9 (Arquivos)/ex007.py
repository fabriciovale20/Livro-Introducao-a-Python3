"""
    Exercício 07

    Crie um programa que leia um arquivo-text e gere um arquivo de saída paginado. Cada linha não deve conter mais e 76 caracteres.
Cada página terá no máximo 60 linhas. Adicione na última linha de cada página o número da página atual e o nome do arquivo original.
"""

pagina = 1
valor_atual = 0

with open('textoex007.txt') as texto:
        for palavras in texto.readlines():
            with open(f'pagina{pagina}.txt', 'w') as pag:
            linhas = 0

                linhas += 1

                if linhas < 60:
                    pag.write(f'{palavras}')
                else:
                    pag.write(f'Pagina {pagina}')
                    pagina += 1
                    linhas = 0
                    valor_atual = linhas

"""
    Exercício 33

    Crie um programa que gere uma página uma página html com links para todos os arquivos jpg e png encontrados a partir de um diretório informado
na linha de comando.
"""

import os.path

arquivo = input('Nome do arquivo: ')

with open("ex033.html", "w", encoding="utf-8") as página:
    página.write("""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
    <meta charset="utf-8">
    <title>Links de Imagens</title>
    </head>
    <body>
    """)

    if os.path.exists(arquivo):
        lista_arquivo = os.listdir(arquivo)
        os.chdir(arquivo)
        caminho = os.getcwd()

        for c in lista_arquivo:
            if 'jpg' in c or 'png' in c:
                página.write(f'<li><a href={caminho}\{c}>{caminho}\{c}</a></li>\n')
    else:
        página.write('<li>Arquivo não existe.</li>')
    página.write("</body></html>")
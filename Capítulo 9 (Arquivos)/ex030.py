"""
    Exercício 30

    Modifique o Programa 9.8 para gerar uma lista html, usando os elementos ul el1. Todos os elementos da lista devem estar dentro do elemento
ul, e cada item dentro de um elemento li.

Exemplo: <ul><li>Item1</li><li>Item2</li><li>Item3</li></ul>V
"""

filmes = {
    "drama": ["Cidadão Kane", "O Poderoso Chefão"],
    "comédia": ["Tempos Modernos", "American Pie", "Dr. Dolittle"],
    "policial": ["Chuva Negra", "Desejo de Matar", "Difícil de Matar"],
    "guerra": ["Rambo", "Platoon", "Tora!Tora!Tora"]
}

with open("filmes.html", "w", encoding="utf-8") as página:
    página.write("""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
    <meta charset="utf-8">
    <title>Filmes</title>
    </head>
    <body>
    """)

    for c, v in filmes.items():
        página.write(f"<ul>{c}</ul>\n")

        for e in v:
            página.write(f"<li>{e}</li>\n")
    página.write("</body></html>")

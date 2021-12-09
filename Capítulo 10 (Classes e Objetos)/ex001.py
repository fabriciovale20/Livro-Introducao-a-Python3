"""
    Exercício 01

    Adicione os atributos tamanho e marca à classe Televisão. Crie dois objetos Televisão e atribua tamanhos e marcas diferentes.
Depois, imprima o valor desses atributos de forma a confirmar a independência dos valores de cada instância (objeto).
"""

class Televisão:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = 0
        self.marca = ''

tv = Televisão()
print(f"""TV
Ligada: {tv.ligada}
Canal: {tv.canal}
Tamanho: {tv.tamanho}
Marca: {tv.marca}""")

tv_sala = Televisão()
tv_sala.ligada = True
tv_sala.canal = 4
tv_sala.tamanho = 51
tv_sala.marca = 'LG'
print(f"""\nTV da Sala
Ligada: {tv_sala.ligada}
Canal: {tv_sala.canal}
Tamanho: {tv_sala.tamanho}
Marca: {tv_sala.marca}""")
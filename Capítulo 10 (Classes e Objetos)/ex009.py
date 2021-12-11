"""
    Exercício 09

    Crie classes para reprensentar estados e cidades. Cada estado tem um nome, sigla e cidades. Cada cidade tem nome e população.
Escreva um programa de testes que crie três estados com algumas cidades em cada um. Exiba a população de cada estado como a soma da
população de suas cidades.
"""

class Estado:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
    

class Cidades:
    def __init__(self, estado):
        self.estado = estado[0].nome
        self.sigla = estado[0].sigla
        self.cidades = []

    def adicionar(self, cidade, população):
        self.cidade = cidade
        self.população = população

        self.cidades.append([self.cidade, self.população])

    def lista(self):
        print('-'*40)
        print(f'{self.estado} - {self.sigla}'.center(40))
        print('-'*40)
        print(f'{" Cidades e habitantes ":=^40}')
        soma = 0

        for c in self.cidades:
            print(f'- {c[0]}, {c[1]} habitantes')
            soma += c[1]

        print(f'\nSoma dos habitantes: {soma}')

rn = Estado('Rio Grande do Norte', 'RN')
cidadesrn = Cidades([rn])

cidadesrn.adicionar('Mossoró', 300)
cidadesrn.adicionar('Natal', 500)
cidadesrn.adicionar('Assu', 800)
cidadesrn.lista()

ce = Estado('Ceará', 'CE')
cidadesce = Cidades([ce])

cidadesce.adicionar('Fortaleza', 253)
cidadesce.adicionar('Beberibe', 412)
cidadesce.adicionar('Canoa Quebrada', 35)
cidadesce.lista()


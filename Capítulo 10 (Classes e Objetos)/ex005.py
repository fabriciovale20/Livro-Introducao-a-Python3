"""
    Exercício 05

    Utilizando a classe Televisão modificada no exercício anterior, crie duas instâncias (objetos), especificando o valor de min e max por nome.
"""

class Televisão:
    def __init__(self, min=2, max=14):
        self.ligada = False
        self.canal = int(input('Canal inicial: '))
        self.cmin = int(input('Canal mínimo: '))
        self.cmax = int(input('Canal máximo: '))
    
    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1
        else:
            self.canal = self.cmin
            
    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
        else:
            self.canal = self.cmax

tv = Televisão()
tv.muda_canal_para_baixo()
print(tv.canal)

tv.muda_canal_para_cima()
print(tv.canal)

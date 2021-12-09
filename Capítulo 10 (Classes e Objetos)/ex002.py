"""
    Exercício 02

    Atualmente, a classe Televisão inicializa o canal com 2. Modifique a classe Televisão de forma a receber o canal inicial em seu construtor.
"""

class Televisão:
    def __init__(self, min, max):
        self.ligada = False
        self.canal = int(input('Canal inicial: '))
        self.cmin = min
        self.cmax = max
    
    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1
            
    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1

tv = Televisão(1, 99)

for x in range(0, 120):
    tv.muda_canal_para_cima()
print(tv.canal)

for x in range(0, 120):
    tv.muda_canal_para_baixo()
print(tv.canal)

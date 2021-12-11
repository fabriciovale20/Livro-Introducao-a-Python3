class numeros:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.soma()
        self.subtração()

    def soma(self):
        return print(f'Soma: {self.a + self.b}')

    def subtração(self):
        print('Subtração: ', end='')
        if self.maior():
            print(f'{self.a - self.b}')
        else:
            print(f'{self.b - self.a}')

    def maior(self):
        return self.a > self.b

    def verificar(self, c):
        outro.__init__(self, c)

class outro:
    def __init__(self, c):
        self.c = c
        print(f'Valor de C: {self.c}')


teste = numeros(4, 2)
teste.verificar(9)
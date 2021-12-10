"""
    Exercício 06

    Altere o programa de forma que a mensagem saldo insuficiente seja exibida caso haja tentativa de sacar mais dinheiro que o saldo disponível.
"""

class Conta:
    def __init__(self, clientes, número, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.número = número
        self.operações = []
        self.deposito(saldo)

    def resumo(self):
        print(f'CC Número: {self.número} Saldo: {self.saldo:10.2f}')

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operações.append(['SAQUE', valor])
        else:
            self.operações.append(['SALDO INSUFICIENTE', 0])
    
    def deposito(self, valor):
        self.saldo += valor
        self.operações.append(['DEPÓSITO', valor])

    def extrato(self):
        print(f'Extrato CC Nº {self.número}\n')

        for o in self.operações:
            print(f'{o[0]:10s} {o[1]:10.2f}')

        print(f'\n  Saldo: {self.saldo:10.2f}\n')

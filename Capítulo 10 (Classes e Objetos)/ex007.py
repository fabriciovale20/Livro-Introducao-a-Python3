"""
    Exercício 07

    Modifique o método resumo da classe Conta para exibir o nome o telefone de cada cliente.
"""

from clientes import Cliente

class Conta:
    def __init__(self, clientes, número, saldo=0):
        self.saldo = 0
        self.clientes = clientes.nome
        self.telefone = clientes.telefone
        self.número = número
        self.operações = []
        self.deposito(saldo)

    def resumo(self):
        print(f'Nome: {self.clientes} Número: {self.telefone} Saldo: {self.saldo:10.2f}\n')

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

        print(f'\n  Saldo: {self.saldo:10.2f}')

class Conta:
    def __init__(self, clientes, número, saldo=0):
        self.saldo = 0
        self.clientes = clientes[0].nome
        self.telefone = clientes[0].telefone
        self.número = número
        self.operações = []
        self.deposito(saldo)

    def resumo(self):
        print(f'Nome: {self.clientes} Número: {self.telefone} Saldo: {self.saldo:10.2f}\n')

    def validador_saque(self, valor):
        if self.saldo >= valor:
            return True
        else:
            return False

    def saque(self, valor):
        if Conta.validador_saque(self, valor):
            self.saldo -= valor
            self.operações.append(['SAQUE', valor])

            print(f'Saque de R$ {valor:.2f} efetuado com sucesso. ({self.clientes})')
        else:
            self.operações.append(['SALDO INSUFICIENTE', 0])

            print(f'Não foi possível realizar o saque de R$ {valor:.2f}. ({self.clientes})')
    
    def deposito(self, valor):
        self.saldo += valor
        self.operações.append(['DEPÓSITO', valor])

    def extrato(self):
        print('-'*33)
        print(f'Extrato CC Nº {self.número}\n')

        for o in self.operações:
            print(f'{o[0]:20s} {o[1]:10.2f}')

        print(f'\n  Saldo: R$ {self.saldo:.2f}')

class ContaEspecial(Conta):
    def __init__(self, clientes, número, saldo=0, limite=0):
        Conta.__init__(self, clientes, número, saldo)
        self.limite = limite

    def validador_saque(self, valor):
        if self.saldo + self.limite >= valor:
            return True
        else:
            False

    def saque(self, valor):
        if ContaEspecial.validador_saque(self, valor):
            self.saldo -= valor
            self.operações.append(['SAQUE', valor])

            print(f'Saque de R$ {valor:.2f} efetuado com sucesso. ({self.clientes})')

        else:
            self.operações.append(['LIMITE INSUFICIENTE', 0])

            print(f'Não foi possível realizar o saque de R$ {valor:.2f}. ({self.clientes})')
        
        print(f'  Conta: {self.clientes}')
        print(f'  Limite: R$ {self.limite:.2f}')
        print(f'  Saldo disponível: R$ {self.limite - abs(self.saldo):.2f}')

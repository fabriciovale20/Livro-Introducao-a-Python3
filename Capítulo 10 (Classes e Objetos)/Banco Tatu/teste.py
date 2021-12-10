from clientes import Cliente
from contas import Conta

joão = Cliente("João da Silva", "777-1234")
maria = Cliente("Maria Silva", "555-4321")

conta1 = Conta([joão], 1, 100)
conta2 = Conta([maria, joão], 2, 500)

conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(250)
conta2.saque(950)

conta1.resumo()
conta1.extrato()

conta2.resumo()
conta2.extrato()
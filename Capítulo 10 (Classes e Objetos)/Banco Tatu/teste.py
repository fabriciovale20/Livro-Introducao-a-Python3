from clientes import Cliente
from bancos import Banco
from contas import Conta, ContaEspecial

joão = Cliente("João da Silva", "777-1234")
maria = Cliente("Maria Silva", "555-4321")

conta1 = Conta([joão], 1, 100)
conta2 = ContaEspecial([maria], 2, 500, 1000)

conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(500)

conta1.extrato()
conta2.extrato()

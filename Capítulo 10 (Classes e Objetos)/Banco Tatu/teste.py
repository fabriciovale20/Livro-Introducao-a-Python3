from clientes import Cliente
from bancos import Banco
from contas import Conta

joão = Cliente("João da Silva", "777-1234")
maria = Cliente("Maria Silva", "555-4321")
josé = Cliente('José Vargas', '9721-3040')

contaJM = Conta([joão, maria], 100)
contaJ = Conta([josé], 10)

tatu = Banco('Tatu')
tatu.abre_conta(contaJM)
tatu.abre_conta(contaJ)
tatu.lista_contas()

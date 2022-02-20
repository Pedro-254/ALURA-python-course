# Funções que garantem que as filhas tenham os métodos necessarios para existir 
from abc import ABCMeta, abstractmethod
from ast import Pass

class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0
        
    def deposita(self, valor):
        self._saldo += valor
    
    # Garante a implementação desse método em todas as subclasses
    @abstractmethod
    def passa_o_mes(self):
        pass
               
    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)


class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimento(Conta):
    pass

conta16 = ContaCorrente(16)
conta16.deposita(1000)

conta17 = ContaPoupanca(16)
conta17.deposita(1000)

contas = [conta16,conta17]

for conta in contas:
    conta.passa_o_mes()
    print(Conta)    

# Can't instantiate abstract class ContaInvestimento with abstract method passa_o_mes
contaI = ContaInvestimento(77)
    


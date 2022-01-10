class Conta:

    def __init__(self, saldo):
        self.saldo = saldo
    
    def extrato(self):
        print(self.saldo)
    
    def saque(self, valor):
        self.saldo -= valor
    
    def deposito(self, valor):
        self.saldo += valor
class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0
        
    def deposita(self, valor):
        self.saldo += valor
            
    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self.codigo, self.saldo)
        
    def deposita_para_todas(valor,contas):
        for i in contas:
            if type(i) is ContaCorrente:
                i.deposita(valor)
            
conta_pedro = ContaCorrente(15)

conta_dani = ContaCorrente(47685)

contas = [10, conta_pedro, conta_dani]

ContaCorrente.deposita_para_todas(1000,contas)
print(contas[0],contas[1],contas[2])
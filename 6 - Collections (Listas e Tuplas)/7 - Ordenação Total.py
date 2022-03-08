from operator import attrgetter

from functools import total_ordering

# Implementa os outro metodos de comparação
@total_ordering

class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0


    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)
    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo and self._saldo == outro._saldo
    # Less than
    def __lt__(self,outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        return self._codigo < outro._codigo

    def deposita(self, valor):
        self._saldo += valor
        
conta_do_guilherme = ContaSalario(1700)
conta_do_guilherme.deposita(500)
conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(500)
conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(500)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]
# Ordenando com um criterio de desempate no attrgetter
for conta in sorted(contas, key=attrgetter("_saldo", "_codigo")):
  print(conta)
  
# Ordenando naturalmente apartir da implementação do criterio na classe
for conta in sorted(contas, key=attrgetter("_saldo", "_codigo")):
  print(conta)

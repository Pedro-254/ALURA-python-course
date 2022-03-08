from operator import attrgetter


class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

    # Less than
    def __lt__(self,outro):
        return self._saldo < outro._saldo

conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(510)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]
# Ordena objetos apartir de um atributo
for conta in sorted(contas, key=attrgetter("_saldo")):
  print(conta)
  
# Apartir da utilização do metodo __lt__ podemos comparar e ordenar
# naturalmente.
print(conta_da_daniela < conta_do_paulo)
for conta in sorted(contas):
  print(conta)
  
  
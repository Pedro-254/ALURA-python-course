from conta import Conta

conta = Conta(123, "Nico", 55.5)
conta2 = Conta(321, "Marco", 100.0, 2000.0)

print(conta.limite)
print(conta2.limite)

conta.limite = 10

print(conta.limite)

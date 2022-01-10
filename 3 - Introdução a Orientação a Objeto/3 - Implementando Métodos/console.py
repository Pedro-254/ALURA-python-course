from conta import Conta

conta = Conta(123, "Nico", 55.5)
conta2 = Conta(321, "Marco", 100.0, 2000.0)

# Acesse o objeto x e chame o extrato
conta.extrato()

conta.deposita(15.0)

conta.extrato()

conta.saca(15.0)

conta.extrato()
from conta import Conta

conta = Conta(123, "Nico", 55.5)

# Nova forma de acessar um objeto pois ele está privado
print(conta._Conta__limite)
# Acessar da maneira convencional se torna impossivel
# print(conta.__limite) (GERA ERRO!)
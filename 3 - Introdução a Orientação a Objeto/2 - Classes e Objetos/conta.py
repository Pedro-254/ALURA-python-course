class Conta:

    # Criação de um objeto
    def __init__(self, numero, titular, saldo, limite = 1000.0):
        print("Construindo objeto...")
        # Dando uma caracteristica para esse objeto que está sendo criado
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

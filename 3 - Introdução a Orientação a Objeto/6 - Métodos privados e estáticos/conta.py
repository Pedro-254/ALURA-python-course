class Conta:

    def __init__(self, numero, titular, saldo, limite = 1000.0):
        print("Construindo objeto...")
        # Dando uma caracteristica para esse objeto que está sendo criado
            # Colocando "__" antes do atributo tornamos ele privado.
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    # Utilizando o "__" antes do método o torna privado
    def __pode_sacar(self, valor_a_sacar):
        return valor_a_sacar <= (self.__saldo + self.__limite)

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor %d passou o limite" % valor)

    # Encapsulamento de metodos
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor
    
    #Metodo estático
    @staticmethod
    def codigo_banco():
        return "001"
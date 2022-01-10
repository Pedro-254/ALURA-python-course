class Cliente:
    def __init__(self, nome):
        self.__nome = nome
    
    #Transforma o método em uma propriedade, tornando desnecessário o uso de "()" para chama-lo
    @property
    def nome(self):
        print("Chamando @property nome()")
        return self.__nome.title()
    
    # Propriedade setter
    @nome.setter
    def nome(self, nome):
        print("Chamando setter nome()")
        self.__nome = nome
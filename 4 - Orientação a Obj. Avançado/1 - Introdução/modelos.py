#Classe mãe, tem as caracteristicas genéricas que serão herdadas pelas filhas
class Programa:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        # Herdando nome e ano da classe mae
        super().__init__(nome, ano)
        self.duracao = duracao

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        # Herdando nome e ano da classe mae
        super().__init__(nome, ano)
        self.temporadas = temporadas

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(vingadores.nome)

atlanta = Serie('atlanta', 2018, 2)
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano}')
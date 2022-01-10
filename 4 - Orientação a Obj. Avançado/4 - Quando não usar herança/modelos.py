class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome
        
    # Representação textual do objeto     
    def __str__ (self):
        return f"{self._nome} - {self.ano} - {self._likes} "
    
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao
        
    # Representação textual do objeto        
    def __str__ (self):
        return f"{self._nome} - {self.ano} - {self.duracao} minutos - {self._likes} "

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas
    
    # Representação textual do objeto     
    def __str__ (self):
        return f"{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} "


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
      
    # Método que torna atributos a sua escolha em listas
    def __getitem__(self, item):
        return self._programas[item]
    
    def __len__(self):
        return len(self._programas)
        
    @property
    def listagem(self):
        return self._programas
        
    @property
    def tamanho(self):
        return len(self._programas)
        


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme("Todo mundo em pânico", 1999, 100)
demolidor = Serie("Demolidor", 2016, 2)

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]

Playlist_fim_de_semana = Playlist("Fim de semana", filmes_e_series)

print()
print("Tamanho da playlist:", len(Playlist_fim_de_semana))
for programa in Playlist_fim_de_semana:
    print(programa)
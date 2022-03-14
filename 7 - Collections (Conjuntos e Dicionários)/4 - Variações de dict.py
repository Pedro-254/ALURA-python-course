meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()
meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()

aparicoes = {}

for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra,0)
    aparicoes[palavra] = ate_agora + 1

for chave,texto in aparicoes.items():
    print(chave, "=", texto)

print("--------------------------------")

# Outra forma de criar um dict com um valor padrao... nesse caso 0 == int()
from collections import defaultdict

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
  ate_agora = aparicoes[palavra]
  aparicoes[palavra] = ate_agora + 1

for chave,texto in aparicoes.items():
    print(chave, "=", texto)
    
    
# Usando o defaultdict em classes
class Conta:
  def __init__(self):
    print("Criando uma conta")

# Dessa forma ao tentar acessar uma conta que não existe o defaultdict ja
# cria uma nova automaticamente.
contas = defaultdict(Conta)
contas[15]
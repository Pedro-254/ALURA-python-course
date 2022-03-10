# Dicionário (dict)
aparicoes = {
  "Guilherme" : 1,
  "cachorro" : 2,
  "nome" : 2,
  "vindo" : 1
}

# Buscando o valor pela chave
print(aparicoes["Guilherme"])
print(aparicoes["cachorro"])

# Deletando um elemento
del aparicoes["cachorro"]

# Dicionarios tem suas chaves como elementos da iteração
for elemento in aparicoes:
    print(elemento)
    
# Podemos acessar os valores com o metodo .values()
for elemento in aparicoes.values():
    print(elemento)
    
# Podemos acessar tbm as duplas de valores, mais conhecidos como items.
for elemento in aparicoes.items():
    print(elemento)
    
for chave,valor in aparicoes.items():
    print(chave, "->", valor)
# Conjuntos são mutáveis!
usuarios = {1,5,76,34,52,13,17}

# add um elemento ao conjunto
usuarios.add(13)

# Mas tambem podem se tornar imutáveis
# Cria um novo cunjunto imutavel.
usuarios = frozenset(usuarios)

# Tirando a duplicidade usando conjunto de strings
meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
print(set(meu_texto.split()))
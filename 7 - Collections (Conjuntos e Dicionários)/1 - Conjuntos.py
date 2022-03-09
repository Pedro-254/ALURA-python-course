# Como copiar uma lista

usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

# Copia a lista
assistiram = usuarios_data_science.copy()
# Extende uma lista com outra lista
assistiram.extend(usuarios_machine_learning)

# Acaba gerando um repetição de elementos não desejada
print(assistiram)

# Utilizando conjuntos... 
usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

# Dessa forma não há repetição!
assistiram = usuarios_data_science | usuarios_machine_learning
print(assistiram)

# Apesar de não ter ordem conjuntos são iteraveis.
for usuarios in assistiram:
    print(usuarios)
idades = [15,87,32,65,56,32,49,37]


# Pega posição
for idade in range(len(idades)):
    print(idade, idades[idade])

# Usando enumerate
print(list(enumerate(idades)))

for indice,idade in enumerate(idades):
    print(indice, "x", idade)
    
usuarios = [
    ("Pedro", 20, 2001),
    ("Joao", 12, 2009),
    ("Marilene", 51, 1970)
]

# Podemos selecionar parte das listas dentro de outra lista com o for
for nome, idade, nascimento in usuarios:
    print(nome)

# Ou ignoralos
for nome, _, _ in usuarios:
    print(nome)
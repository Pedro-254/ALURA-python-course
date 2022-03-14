#  Testando o uso de diversas coleções

from collections import Counter
texto1 = """
Dictionaries are used to store data using the key-value structure in Python.

When you re working with dictionaries, you may ask yourself, how can I add an item to a dictionary? This article will answer that question.

Well break down the basics of dictionaries, how they work, and how you can add an item to a Python dictionary. By the end of this tutorial, you’ll be an expert at adding items to Python dictionaries.

Python Dictionary: A Refresher
The dictionary data structure allows you to map keys to values. This is useful because keys act as a label for a value, which means that when you want to access a particular value, all you have to do is reference the key name for the value you want to retrieve.

Dictionaries generally store information that is related in some way, such as a record for a student at school, or a list of colors in which you can purchase a rug.

Consider the following dictionary:
"""



def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())

    proporcoes = [(letra, frequencia/total_de_caracteres) for letra, frequencia in aparicoes.items()]

    proporcoes = Counter(dict(proporcoes))
    for char,proporcao in proporcoes.most_common(10):
        print("Letra \"{}\" aparece em {:.2f}% do texto".format(char,proporcao*100))
    
analisa_frequencia_de_letras(texto1)
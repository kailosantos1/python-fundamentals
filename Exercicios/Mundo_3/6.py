palavras = ('moto', 'correia', 'bicicleta', 'bola', 'hgjk')
vogais = ('a','e','i','o','u')
palavras_vogais = tuple()

for lista in range(0, len(palavras)):
    mostrar_palavras = palavras[lista]
    palavras_vogais = tuple()
    for lista_vogais in range(0, len(vogais)):
        mostrar_vogais = vogais[lista_vogais]
        if mostrar_vogais in mostrar_palavras:
            palavras_vogais += (mostrar_vogais,)
    print(f"a palavra {mostrar_palavras}, tem as vogais: {palavras_vogais}" )
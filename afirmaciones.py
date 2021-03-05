#assert <expresion booleana> , <mensaje de error>

def primera_letra(lista_de_palabras):
    primeras_letras = []

    for palabra in lista_de_palabras:
        assert type(palabra) == str, f'{palabra} no es un str'
        assert len(palabra) > 0, 'No se permiten str vacios'
        print(len(palabra))

        primeras_letras.append(palabra[0])
    return primeras_letras

print(primera_letra(['alo', 'Hola']))
def raiz():
    objetivo = int(input('Escoje un número '))
    epsilon = 0.0000000001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto+bajo)/2

    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        respuesta = (alto + bajo) / 2
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
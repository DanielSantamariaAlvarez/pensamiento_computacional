
#repaso de if


def operaciones_id():
    if edad_1 == edad_2:
        print('Wow, los dos tienen la misma edad!')
    elif edad_1 > edad_2:
        print(f'{nombre_1} es mayor que {nombre_2}')
    else:
        print(f'{nombre_2} es mayor que {nombre_1}')



if __name__ == '__main__':
    nombre_1 = input('Hola! Como te llamas? ')
    edad_1 = int(input(f'Cual es tu edad, {nombre_1}? '))

    nombre_2 = input('y como se llama tu compañer@? ')
    edad_2 = int(input(f'Cual es tu edad, {nombre_2}? '))



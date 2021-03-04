import busqueda_binaria as raiz

if __name__ == '__main__':
    print('Hola!')
    print('Quieres saber la raiz de algún numero?')
    print('1. Si')
    print('2. No')
    decision = int(input())
    if decision == 1:
        raiz.raiz()
    else:
        print('Ni modos, para otra ocación será =3')
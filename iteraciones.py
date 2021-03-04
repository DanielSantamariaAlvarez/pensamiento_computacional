contador_externo = 0
contador_interno = 0
while contador_externo < 5:
    while contador_interno < 6:
        print(contador_externo, contador_interno)
        contador_interno += 1

        if contador_interno >=3:
            break
    contador_externo +=1
    contador_interno = 0

#----- Funcion iter -------------------------------
palabra_a_iterar = 'Hola_mundo'
iterador = iter(palabra_a_iterar)
print(next(iterador)) #imprime H
print(next(iterador)) #imprime o
print(next(iterador)) #imprime l
print(next(iterador)) #imprime a
#y así sucesivamente, guarda en que va la iteración



    


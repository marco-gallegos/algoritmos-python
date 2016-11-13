def qs(lista, lim_izq, lim_der):
    pivote = int((lim_izq + lim_der) / 2)
    derecha = lim_der
    izquierda = lim_izq

    while izquierda <= derecha:

        while lista[izquierda] < lista[pivote]:
            izquierda += 1
        
        while lista[derecha] > lista[pivote]:
            derecha -= 1

        if izquierda <= derecha:
            lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]
            izquierda += 1
            derecha -= 1

    if izquierda < lim_der:
        qs(lista, izquierda, lim_der)
    
    if derecha > lim_izq:
        qs(lista, lim_izq, derecha)


def quicksort(Lista, tamano):
    qs(Lista, 0, tamano)


# lst = [9, 2, 8, 1, 6]

# qs(lst, 0, (len(lst) - 1))

# print(lst)

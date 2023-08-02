lista = [8, 4, 2, 6, 5, 3, 9, 7]

def ordenar(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = []
    mayores = []

    for i in range(1, len(lista)):
        if lista[i] < pivote:
            menores.append(lista[i])
        else:
            mayores.append(lista[i])

    menores = ordenar(menores)
    mayores = ordenar(mayores)

    return menores + [pivote] + mayores

lista_ordenada = ordenar(lista)
print("Lista ordenada:", lista_ordenada)
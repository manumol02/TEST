def elementos(lista, objetivo):
    diccionario = {}
    for num in lista:
        complemento = objetivo - num
        if complemento in diccionario:
            return [complemento, num]
        diccionario[num] = True
    return []


lista = [3, 6, 9, 12, 4, 1]
objetivo = 10
resultado = elementos(lista, objetivo)
print(resultado) 
lista = [3, 8, 4, 1, 9, 4, 2, 10]
burbuja= True  
while burbuja:
    burbuja = False 
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            burbuja= True  

print(lista)





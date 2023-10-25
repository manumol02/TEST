def bubbleSort(lista):
    
    longitud=len(lista)-1
    iteraciones=0

    for i in range(0,longitud):
       
        for j in range(0,longitud-i):
            
            if lista[j]>lista[j+1]:
               
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
            iteraciones +=1
            
            print(f"{iteraciones}: {lista}")
    return lista
        
lista= [ -1,-80,-59,-30,-40,-90]
print("lista ordenada",bubbleSort(lista))











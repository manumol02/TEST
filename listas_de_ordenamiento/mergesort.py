def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    
    longitud = len(numbers)

    mitad= longitud //2 

    primera_mitad= numbers[:mitad]
    segunda_mitad = numbers[mitad:]
    

    primera_mitad=merge_sort(primera_mitad)
    segunda_mitad=merge_sort(segunda_mitad)

    resultado=[]    
    i, j = 0, 0

    while i < len(primera_mitad) and j < len(segunda_mitad):
        if primera_mitad[i] < segunda_mitad[j]:
            resultado.append(primera_mitad[i])
            i += 1
         
        else:
            resultado.append(segunda_mitad[j])
            j += 1 
  
    resultado.extend(primera_mitad[i:])
    resultado.extend(segunda_mitad[j:]) 
    return resultado


numbers = [4,3,2,1,9,8,7,6,5]

lista_ordenada = merge_sort(numbers)

print("Lista ordenada:",lista_ordenada)



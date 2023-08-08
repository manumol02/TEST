def recursiveReverseString(cadena_principal):
   
    if len(cadena_principal) <= 1:
        return cadena_principal

    return cadena_principal[-1] + recursiveReverseString(cadena_principal[:-1]) 

cadena_principal="perro"
cadena_invertida= recursiveReverseString(cadena_principal)
print("cadena original",cadena_principal)
print("cadena invertida",cadena_invertida)


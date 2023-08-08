def distancia(numeros):
    if not numeros or len(numeros) < 2:
        return "No hay suficientes números para calcular el número menor y mayor"

    menor = min(numeros)
    mayor = max(numeros)
    max_diff = max(numeros)-min(numeros)

    return menor, mayor,max_diff

numeros = [7, 2, 9, 5, 1, 6]
resultado_min,resultado_max ,max_diff= distancia(numeros)

print(max_diff,"the maximum difference is between", resultado_min,"and",resultado_max)


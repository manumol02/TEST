def max_difference(nums):
    if not nums or len(nums) < 2:
        return "No hay suficientes números para calcular la diferencia máxima"

    menor= nums[0]
    max_diff = nums[1] - nums[0]

    for i in range(1, len(nums)):
        comparacion = nums[i] - menor
        if comparacion> max_diff:
            max_diff = comparacion
        if nums[i] < menor:
            menor= nums[i]

    return max_diff

numeros =  [7, 1, 9, 5, 2, 6]

maxima_diferencia = max_difference(numeros)

print("La máxima diferencia es", maxima_diferencia)



def calcular_total(autos: list[int]) -> int:
    total = None

    for cantidad in autos:
        if not total:
            total = cantidad
        else:
            total += cantidad

    return total

def ordenar_matriz(matriz: list[list], index: int, sentido: str='DES') -> list[list]:
    nueva_matriz = [[]] * len(matriz)

    for i in range(len(matriz[0])-1):
        i_valor = None
        for j in range(1, len(matriz[0])):
            if (matriz[index][j] < matriz[index][i] and sentido == 'ASC') or (matriz[index][j] > matriz[index][i] and sentido == 'DES'):
                for k in range(len(matriz)):
                    nueva_matriz[k].append(matriz[k][j])

    print(nueva_matriz)
    return nueva_matriz

def calcular_ganancia_garage(valor_a, valor_b) -> int:
    return valor_a * valor_b

def calcular_garages_6(matriz: list[list]) -> int:
    total = 0

    for i in matriz[2]:
        if i >= 6 and total:
            total += 1
        elif i >= 6 and not total:
            total = 1

    return total

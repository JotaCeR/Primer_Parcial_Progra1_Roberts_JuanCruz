from auxiliares import calcular_ganancia_garage

def obtener_recaudacion(matriz: list[list]) -> None:
    total = None

    for i in range(len(matriz[0])):
        matriz[4][i] = calcular_ganancia_garage(matriz[2][i], matriz[3][i])

        if not total:
            total = calcular_ganancia_garage(matriz[2][i], matriz[3][i])
        else:
            total += calcular_ganancia_garage(matriz[2][i], matriz[3][i])
        

    reporte = f'''
    La ganancia total obtenida
    con la sumatoria de todos
    los garages arroja un total
    de ${total} pesos
    '''

    print(reporte)

from auxiliares import calcular_ganancia_garage

def obtener_recaudacion(matriz: list[list]) -> None:
    total = None

    for i in range(len(matriz[0])):
        garage = []
        for j in range(len(matriz)):
            garage.append(matriz[j][i])
        if not total:
            total = calcular_ganancia_garage(garage)
        else:
            total += calcular_ganancia_garage(garage)

    reporte = f'''
    La ganancia total obtenida
    con la sumatoria de todos
    los garages arroja un total
    de ${total} pesos
    '''

    print(reporte)

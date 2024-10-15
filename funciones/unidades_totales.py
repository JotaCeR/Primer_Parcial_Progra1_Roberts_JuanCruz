from auxiliares import calcular_total

def calcular_unidades_totales(matriz: list[list]) -> None:
    existencias = calcular_total(matriz[2])
    reporte = f'''
    La cantidad total de vehículos
    en posesión de la concesionaria
    es de {existencias} unidades.
    '''

    print(reporte)
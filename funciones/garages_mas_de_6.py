from auxiliares import calcular_garages_6

def calcular_garages_6_mas(matriz: list[list]) -> None:
    garages = calcular_garages_6(matriz)

    reporte = f'''
    La concesionaria cuenta
    con un total de {garages} garages
    albergando 6 vehículos o más.
    '''

    print(reporte)
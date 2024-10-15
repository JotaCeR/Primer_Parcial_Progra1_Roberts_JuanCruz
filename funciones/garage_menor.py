from auxiliares import ordenar_matriz

def garage_con_menos_unidades(matriz: list[list]) -> None:
    matriz_ordenada = ordenar_matriz(matriz, 2)

    reporte = f'''
    El garage con menos unidades
    almacenadas presenta el sig-
    uiente informe:
    {matriz_ordenada[2][0]} {matriz_ordenada[0][0]} {matriz_ordenada[1][0]}
    con un valor de ${matriz_ordenada[3][0]} y
    una ganancia estimada de ${matriz_ordenada[2][0]*matriz_ordenada[3][0]}
    '''

    print(reporte)
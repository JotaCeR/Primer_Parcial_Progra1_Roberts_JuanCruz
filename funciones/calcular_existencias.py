from auxiliares import (marcas, modelos)


def calcular_existencias(matriz: list[list]) -> list[list]:

    for i in range(len(matriz[0])):
        linea = ""
        garage = i+1
        print(f"Garage N°{garage}:")
        for j in range(len(matriz)):
            linea += f"| {matriz[j][i]} "
        print(linea[:-1])

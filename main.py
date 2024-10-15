from UTN_Heroes_Dataset.utn_pp import (get_original_matrix, mostrar_matriz_texto_tabla)
from funciones import (calcular_existencias, calcular_unidades_totales, garage_con_menos_unidades,
                       obtener_recaudacion, calcular_garages_6_mas)
from auxiliares import mostrar_menu
import math

casa_matriz = get_original_matrix()

def main_menu() -> None:

    while True:
        mostrar_menu()
        eleccion = int(input(''))

        if eleccion == 1:
           calcular_existencias(casa_matriz)
        elif eleccion == 2:
           calcular_unidades_totales(casa_matriz)
        elif eleccion == 5:
           obtener_recaudacion(casa_matriz)
        elif eleccion == 6:
           calcular_garages_6_mas(casa_matriz)
        elif eleccion == 9:
           break
        elif eleccion > 9 and eleccion >= 1:
           print("Funcionalidades en desarrollo...")
        else:
           print("Por favor elija una opción válida.")
            


if __name__ == '__main__':
    
    # calcular_existencias(casa_matriz)
    # calcular_unidades_totales(casa_matriz)
    # garage_con_menos_unidades(casa_matriz)
    # obtener_recaudacion(casa_matriz)
    # calcular_garages_6_mas(casa_matriz)
    main_menu()
from UTN_Heroes_Dataset.utn_pp import (get_original_matrix, mostrar_matriz_texto_tabla)
from funciones import (calcular_existencias, calcular_unidades_totales, garage_con_menos_unidades, obtener_recaudacion)
'''
Marca, Modelo, Cantidad, Valor, Undefined
'''

casa_matriz = get_original_matrix()

if __name__ == '__main__':
    
    # calcular_existencias(casa_matriz)
    # calcular_unidades_totales(casa_matriz)
    # garage_con_menos_unidades(casa_matriz)
    obtener_recaudacion(casa_matriz)
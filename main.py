from UTN_Heroes_Dataset.utn_pp import (get_original_matrix, mostrar_matriz_texto_tabla)
from funciones import calcular_existencias
'''
Marca, Modelo, Cantidad, KM's/Valor, Undefined
'''

casa_matriz = get_original_matrix()

if __name__ == '__main__':
    
    calcular_existencias(casa_matriz)
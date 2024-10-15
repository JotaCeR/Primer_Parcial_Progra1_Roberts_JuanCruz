from UTN_Heroes_Dataset.utn_pp import clear_console

def mostrar_menu() -> None:
    clear_console()
    menu = '''
    Por favor seleccione una opción:
    [1] Obtener existencias
    [2] Obtener total de unidades almacenadas
    [3] —
    [4] —
    [5] Obtener recaudación
    [6] Obtener garages con 6 o más vehículos
    [7] —
    [8] —
    [9] Finalizar

    . .  .
    '''
    
    print(menu)


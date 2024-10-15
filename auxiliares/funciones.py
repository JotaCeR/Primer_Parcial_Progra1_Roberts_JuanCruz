
def calcular_total(autos: list[int]) -> int:
    total = None

    for cantidad in autos:
        if not total:
            total = cantidad
        else:
            total += cantidad

    return total
# ========================================
# Función count_sheeps para contar ovejas
# ========================================

# Versión original
def count_sheeps(sheep):
    """
    Cuenta cuántos True (ovejas presentes) hay en la lista de entrada.
    
    Args:
        sheep (list): Lista de elementos booleanos y None, donde True indica la presencia de una oveja.
    
    Returns:
        int: Cantidad de ovejas presentes (True) en la lista.
    """
    count = 0  # Inicializamos un contador a cero para contar las ovejas presentes.
    for s in sheep:  # Iteramos sobre cada elemento en la lista.
        if s is True:  # Comprobamos si el elemento es True (oveja presente).
            count += 1  # Incrementamos el contador por cada oveja presente.
    return count  # Devolvemos el total de ovejas presentes.

# Versión refactorizada con comprensión de listas
def count_sheeps_refactored(sheep):
    """
    Utiliza comprensión de listas para contar de forma concisa las ovejas presentes en la lista.
    
    Args:
        sheep (list): Lista que puede contener booleanos y None.
        
    Returns:
        int: Número total de True en la lista.
    """
    return sum(1 for s in sheep if s is True)  # Sumamos 1 por cada True encontrado en la lista.

# Ejemplo de uso:
sheep_list = [True, False, True, None, True, False]
print(f"Original: {count_sheeps(sheep_list)}")  # Salida: 3
print(f"Refactorizado: {count_sheeps_refactored(sheep_list)}")  # Salida: 3

# ========================================
# Fin del Documento
# ========================================
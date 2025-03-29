# ========================================
# Función xo para contar 'x' y 'o' en una cadena
# ========================================

# Versión original
def xo(string):
    """
    Evalúa si una cadena contiene el mismo número de 'x' y 'o'.

    Args:
        string (str): Cadena a analizar.

    Returns:
        bool: True si la cantidad de 'x' y 'o' es igual, False de lo contrario.
    """
    string = string.lower()  # Convierte la cadena a minúsculas para neutralizar la distinción entre mayúsculas y minúsculas
    count_x = string.count('x')  # Cuenta las 'x' en la cadena
    count_o = string.count('o')  # Cuenta las 'o' en la cadena
    return count_x == count_o  # Compara las cuentas y devuelve True si son iguales, False si no

# Refactorización con comprensión de listas y método sum()
def xo_refactored(string):
    """
    Versión refactorizada que utiliza métodos de Python más avanzados para contar 'x' y 'o'.

    Args:
        string (str): Cadena a analizar.

    Returns:
        bool: Devuelve True si hay igual número de 'x' y 'o', False en caso contrario.
    """
    string = string.lower()  # Normaliza la cadena a minúsculas
    return string.count('x') == string.count('o')  # Devuelve directamente el resultado de la comparación de conteos

# Ejemplo de uso:
test_string = "OxoxoXox"
print(xo(test_string))  # Salida: True
print(xo_refactored(test_string))  # Salida: True

# ========================================
# Fin del Documento
# ========================================
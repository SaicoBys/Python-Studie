# ========================================
# Función boolean_to_string para Convertir Booleanos a Cadena
# ========================================

# Versión original
def boolean_to_string(b):
    """
    Convierte un valor booleano en su representación de cadena.

    Args:
        b (bool): Valor booleano a convertir.

    Returns:
        str: Representación de cadena del valor booleano.
    """
    return str(b)  # Convierte el booleano 'b' a cadena y devuelve el resultado.

# Refactorización (opcional, ya que la función es bastante simple)
def boolean_to_string_refactored(b):
    """
    Versión simplificada que directamente devuelve la conversión a cadena de un booleano.
    
    Args:
        b (bool): Valor booleano para convertir.

    Returns:
        str: Cadena "True" o "False" dependiendo del valor de 'b'.
    """
    return "True" if b else "False"  # Utiliza expresión condicional para convertir y devolver la cadena.

# Ejemplo de uso:
boolean_value = True
print(boolean_to_string(boolean_value))  # Salida: "True"
print(boolean_to_string_refactored(boolean_value))  # Salida: "True"

# ========================================
# Fin del Documento
# ========================================
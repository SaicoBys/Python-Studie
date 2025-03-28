# ========================================
# Función smash para combinar palabras en una oración
# ========================================

# Descripción:
"""
Esta función toma una lista de palabras y las combina en una única oración, separando cada palabra con un espacio.
Es útil para construir oraciones a partir de palabras individuales de manera eficiente y clara.
"""

# Implementación de la función:
def smash(words):
    """
    Combina una lista de palabras en una oración, utilizando el método join de cadenas.
    
    Args:
        words (list): Una lista de strings que representan las palabras a unir.
    
    Returns:
        str: Una cadena que representa la oración formada al unir las palabras con espacios.
    """
    return " ".join(words)  # El método 'join' concatena elementos de la lista 'words', insertando un espacio entre cada uno.

# Ejemplo de uso:
word_list = ["hello", "world", "this", "is", "great"]
sentence = smash(word_list)
print(sentence)  # Salida: "hello world this is great"

# ========================================
# Fin del Documento
# ========================================
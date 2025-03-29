# ========================================
# Función disemvowel para eliminar vocales
# ========================================

# Descripción:
"""
Esta función elimina todas las vocales de una cadena dada.
Se proporcionan dos implementaciones: una usando un bucle for
y otra utilizando comprensión de listas.
"""

# Versión con bucle for
def disemvowel(string_):
    vowels = "aeiouAEIOU"  # Definimos una cadena con todas las vocales a eliminar.
    result = ""  # Inicializamos una cadena vacía para guardar el resultado.
    for char in string_:  # Iteramos sobre cada carácter de la cadena dada.
        if char not in vowels:  # Verificamos si el carácter no es una vocal.
            result += char  # Si no es vocal, lo agregamos al resultado.
    return result  # Devolvemos la cadena resultante.

# Versión con comprensión de listas
def disemvowel_comprehension(string_):
    vowels = "aeiouAEIOU"  # Definimos las vocales a eliminar.
    return ''.join(char for char in string_ if char not in vowels)  # Usamos comprensión de listas para crear y devolver la nueva cadena.

# Ejemplo de uso:
input_string = "This website is for losers LOL!"
print(disemvowel(input_string))  # Salida: "Ths wbst s fr lsrs LL!"
print(disemvowel_comprehension(input_string))  # Salida: "Ths wbst s fr lsrs LL!"

# ========================================
# Fin del Documento
# ========================================
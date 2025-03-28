# ========================================
# Rebanado de Listas en Python
# ========================================

# Descripción:
"""
El rebanado de listas te permite extraer porciones específicas de una lista utilizando una sintaxis concisa.
Puedes especificar dónde comienza y termina el segmento que quieres extraer.
"""

# Lista de ejemplo
letters = ["a", "b", "c", "d", "e", "f", "g"]
print("Lista original:", letters)

# Extraer sublista desde el índice 1 al 5
sliced_list = letters[1:6]
print("Sublista desde 'b' hasta 'f':", sliced_list)

# Extraer los últimos tres elementos
print("Últimos tres elementos:", letters[-3:])

# Extraer todos excepto los dos últimos elementos
print("Todos excepto los dos últimos:", letters[:-2])

# ========================================
# Fin del Documento
# ========================================

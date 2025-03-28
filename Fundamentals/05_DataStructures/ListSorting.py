# ========================================
# Ordenamiento de Listas en Python
# ========================================

# Descripción:
"""
Python ofrece métodos incorporados para ordenar listas, ya sea directamente o creando una nueva lista ordenada.
"""

# Lista de nombres
names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
print("Lista original:", names)

# Ordenar la lista de forma ascendente
names.sort()
print("Lista ordenada:", names)

# Ordenar la lista de forma descendente
names.sort(reverse=True)
print("Lista ordenada en orden descendente:", names)

# Crear una nueva lista ordenada sin alterar la original
sorted_names = sorted(names)
print("Nueva lista ordenada:", sorted_names)
print("Lista original sin cambios:", names)

# ========================================
# Fin del Documento
# ========================================

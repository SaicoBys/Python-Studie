# ========================================
# Trabajando con Listas 2D en Python
# ========================================

# Descripción de Acceso a Listas 2D:
"""
Para acceder a elementos en listas 2D, especificamos dos índices: uno para la sublista y otro para el elemento dentro de esa sublista.
"""

# Lista 2D de alturas de estudiantes
heights = [["Noelle", 61], ["Ali", 70], ["Sam", 67]]

# Acceder a la altura de Noelle
noelles_height = heights[0][1]
print("Altura de Noelle:", noelles_height)

# Descripción de Modificación de Listas 2D:
"""
Para modificar elementos en listas 2D, usamos índices para apuntar al elemento específico dentro de las sublistas.
"""

# Lista 2D de nombres y hobbies
class_name_hobbies = [["Jenny", "Breakdancing"], ["Alexus", "Photography"], ["Grace", "Soccer"]]

# Cambiar el hobby de Jenny a 'Meditation'
class_name_hobbies[0][1] = "Meditation"
print("Hobbies después de la modificación:", class_name_hobbies)

# ========================================
# Fin del Documento
# ========================================
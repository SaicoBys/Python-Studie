# ========================================
# Indexación y Manipulación de Listas en Python
# ========================================

# Descripción de la Indexación:
"""
La indexación en las listas te permite acceder a elementos individuales.
Python utiliza indexación basada en cero, lo que significa que el primer elemento de la lista tiene índice 0.
"""

# Lista de ejemplo con nombres de jugadores
names = ['Roger', 'Rafael', 'Andy', 'Novak']
print("El tercer jugador es:", names[2])  # Accede al tercer elemento, que es 'Andy'

# Indexación negativa para acceder al último elemento
print("El último jugador es:", names[-1])  # Accede al último elemento, que es 'Novak'

# Descripción del Método .insert():
"""
El método .insert() se utiliza para agregar un elemento a una lista en un índice especificado.
"""

# Lista de nombres en una fila
store_line = ["Karla", "Maxium", "Martim", "Isabella"]

# Insertar a 'Vikor' en la segunda posición
store_line.insert(2, "Vikor")
print("Lista después de insertar:", store_line)

# Descripción del Método .pop():
"""
El método .pop() elimina el elemento en el índice dado de la lista y lo devuelve.
Si no se especifica un índice, .pop() elimina y devuelve el último elemento de la lista.
"""

# Lista de temas de ciencia de la computación
cs_topics = ["Python", "Data Structures", "Balloon Making", "Algorithms", "Clowns 101"]

# Eliminar el último elemento
removed_element = cs_topics.pop()
print("Lista después de pop:", cs_topics)
print("Elemento eliminado:", removed_element)

# ========================================
# Fin del Documento
# ========================================
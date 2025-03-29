# ========================================
"""
📌 TEMA: Indexación y Manipulación de Listas

La indexación te permite acceder, insertar y eliminar elementos en listas.

✅ Características:
- Python usa indexación basada en cero.
- Puedes usar índices negativos para acceder desde el final.
- `.insert()` permite agregar elementos en posiciones específicas.
- `.pop()` elimina y devuelve un elemento de la lista (último por defecto).
"""
# ========================================


# --------------------------------------------------
# 🎯 Ejemplo 1: Acceso con índice positivo y negativo
# --------------------------------------------------
"""
Accedemos al tercer y último jugador en una lista de nombres.
"""

names = ['Roger', 'Rafael', 'Andy', 'Novak']       # Lista de jugadores
print("El tercer jugador es:", names[2])           # Accede al índice 2 → 'Andy'
print("El último jugador es:", names[-1])          # Accede al índice -1 → 'Novak'


# --------------------------------------------------
# 🎯 Ejemplo 2: Uso del método .insert()
# --------------------------------------------------
"""
Insertamos un nuevo elemento en una posición específica dentro de la lista.
"""

store_line = ["Karla", "Maxium", "Martim", "Isabella"]  # Lista inicial
store_line.insert(2, "Vikor")                            # Inserta "Vikor" en el índice 2
print("Lista después de insertar:", store_line)         # Muestra la lista actualizada


# --------------------------------------------------
# 🎯 Ejemplo 3: Uso del método .pop()
# --------------------------------------------------
"""
Eliminamos el último elemento de la lista usando .pop() y lo mostramos.
"""

cs_topics = ["Python", "Data Structures", "Balloon Making", "Algorithms", "Clowns 101"]  # Lista de temas
removed_element = cs_topics.pop()                        # Elimina el último elemento
print("Lista después de pop:", cs_topics)               # Muestra la lista actualizada
print("Elemento eliminado:", removed_element)           # Muestra el elemento eliminado


# ========================================
"""
📌 RESUMEN

- Se accede a elementos con `lista[indice]`.
- Se puede usar índice negativo para acceder desde el final.
- `.insert(indice, elemento)` agrega un valor en una posición específica.
- `.pop()` elimina y devuelve un elemento (último por defecto).
"""
# ========================================


# ========================================
"""
## 🧠 Ejercicios de Práctica
Practica lo aprendido sobre indexación y métodos de listas.
"""
# ========================================

# --------------------------------------------------
# 1️⃣ Acceder a Elementos por Índice
# --------------------------------------------------
"""
Crea una lista de 5 países y muestra el segundo y el último país usando índices.
"""

# Tu código aquí...


# --------------------------------------------------
# 2️⃣ Insertar un Elemento
# --------------------------------------------------
"""
Crea una lista de animales. Inserta 'Lobo' en la posición 2.
Imprime la lista resultante.
"""

# Tu código aquí...


# --------------------------------------------------
# 3️⃣ Eliminar con .pop()
# --------------------------------------------------
"""
Crea una lista de comidas y elimina la tercera usando `.pop()`.
Muestra la comida eliminada y la lista final.
"""

# Tu código aquí...

# ========================================
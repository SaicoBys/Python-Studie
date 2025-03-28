# ========================================
# Introducción a las Estructuras de Datos en Python
# ========================================

"""
## 📌 Descripción
Las estructuras de datos en Python permiten almacenar y organizar información de manera eficiente.
Las principales estructuras incluyen:

✔ **Listas** (`list`) → Colecciones ordenadas y mutables.  
✔ **Tuplas** (`tuple`) → Similares a las listas, pero inmutables.  
✔ **Conjuntos** (`set`) → Colecciones desordenadas sin duplicados.  
✔ **Diccionarios** (`dict`) → Pares clave-valor para almacenamiento estructurado.

Cada una de estas estructuras tiene usos específicos y características únicas.
"""

# ========================================
# 1. Listas en Python
# ========================================

"""
📌 **Listas (`list`)**
Las listas son colecciones ordenadas y mutables. Permiten almacenar elementos de cualquier tipo.
Más detalles en `ListBasics.py`.
"""

# Lista de ejemplo
mi_lista = [1, 2, 3, 4, 5]
print(mi_lista)  # Salida: [1, 2, 3, 4, 5]

# ========================================
# 2. Tuplas en Python
# ========================================

"""
📌 **Tuplas (`tuple`)**
Son similares a las listas, pero inmutables (no se pueden modificar después de su creación).
"""

mi_tupla = (10, 20, 30)
print(mi_tupla)  # Salida: (10, 20, 30)

# ========================================
# 3. Conjuntos en Python
# ========================================

"""
📌 **Conjuntos (`set`)**
Estructuras desordenadas que no permiten elementos duplicados.
"""

mi_conjunto = {1, 2, 3, 3, 4}
print(mi_conjunto)  # Salida: {1, 2, 3, 4}

# ========================================
# 4. Diccionarios en Python
# ========================================

"""
📌 **Diccionarios (`dict`)**
Colección de pares clave-valor, útil para almacenar datos estructurados.
"""

mi_diccionario = {"nombre": "Carlos", "edad": 25}
print(mi_diccionario["nombre"])  # Salida: Carlos

# ========================================
# Fin del Documento
# ========================================

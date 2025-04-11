# ========================================
"""
📘 TEMA: modules_overview - Python Modules, Namespaces, and Scope

🔹 Un módulo en Python es un archivo `.py` que contiene código reutilizable: funciones, clases o variables.
🔹 Puedes importar estos módulos para no repetir código y organizar mejor tus programas.
🔹 Python viene con una Standard Library (librería estándar) llena de módulos listos para usar.

🔧 FORMAS DE IMPORTAR:
- import modulo
- from modulo import funcion
- import modulo as alias
- from modulo import * ❌ (desaconsejado porque contamina el namespace)

🔐 NAMESPACE:
- Cada módulo tiene su propio espacio de nombres (namespace), lo que evita conflictos con variables locales.
- Ejemplo: `random.randint(1, 10)` ← el nombre `randint` vive dentro del módulo `random`.

🧠 ALIAS:
- Puedes renombrar un módulo con `as` para escribir menos o evitar conflictos:
  import matplotlib.pyplot as plt

📁 SCOPE ENTRE ARCHIVOS:
- Cada archivo `.py` tiene su propio scope (ámbito).
- Para usar funciones o variables de otro archivo del mismo proyecto, debes importarlas explícitamente:
  from sandwiches import sandwiches
"""
# ========================================


# 🔹 MÓDULO: random
import random

# Crear una lista con 101 números aleatorios entre 1 y 100
random_list = [random.randint(1, 100) for _ in range(101)]

# Elegir un número aleatorio de la lista
random_number = random.choice(random_list)

print("Número aleatorio elegido:", random_number)


# 🔹 MÓDULO: decimal
from decimal import Decimal

# Usando float (puede causar errores de precisión)
float_total = 0.10 + 0.35
print("Total con float:", float_total)  # 0.44999999999999996 ❌

# Usando Decimal para obtener precisión exacta
decimal_total = Decimal('0.10') + Decimal('0.35')
print("Total con Decimal:", decimal_total)  # 0.45 ✅


# 🔹 SCOPE ENTRE ARCHIVOS (simulado)
# Supón que tienes un archivo llamado sandwiches.py con esto:
# sandwiches = ["jamón", "queso", "pollo"]

# Y en otro archivo (hungry_people.py), puedes hacer esto:
# from sandwiches import sandwiches
# print("Sandwiches disponibles:", sandwiches)


# ========================================
"""
📌 RESUMEN:

✔️ Un módulo es un archivo con código reutilizable que puedes importar.
✔️ Python tiene una librería estándar con módulos muy útiles: `random`, `decimal`, `math`, `datetime`, etc.
✔️ Usa `import` o `from x import y` para traer código desde otro módulo.
✔️ Evita `from x import *` porque puede causar conflictos de nombres.
✔️ Puedes instalar módulos externos con `pip install nombre_modulo`.
✔️ Cada archivo tiene su propio scope: importa explícitamente lo que necesitas.

🔗 Más info: https://docs.python.org/3/library/
"""
# ========================================


# ========================================
# 🧪 EJERCICIOS DE PRÁCTICA
# ========================================

# 1. Usa random.sample() para obtener 5 números únicos del 1 al 20.
# 2. Importa el módulo math como "m" y usa m.floor(3.7).
# 3. Simula tener dos archivos e importa una lista desde uno al otro.
# 4. Usa Decimal para calcular 0.2 + 0.4 con precisión exacta.
# 5. Crea tu propio módulo llamado "utilidades.py" con una función saludar(nombre)
#    y luego impórtala desde otro archivo.

# Espacio para resolver los ejercicios 👇
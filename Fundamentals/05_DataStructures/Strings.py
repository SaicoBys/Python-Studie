# ========================================
# Uso de Strings en Python
# ========================================

"""
## 📌 Descripción:
Los strings son secuencias de caracteres. Se definen con comillas simples o dobles.
Son inmutables, lo que significa que no se pueden modificar directamente.
"""

# ========================================
# Crear y mostrar un string
# ========================================

greeting = "Hello, Jacob!"
print(greeting)

# ========================================
# Métodos comunes de strings
# ========================================
"""
Usamos métodos comunes de strings para transformar o analizar su contenido.
Estos métodos NO modifican el string original, sino que devuelven uno nuevo.
"""

text = "  Python is AWESOME!  "  # String original con espacios

print(text.lower())       # Convierte todo el texto a minúsculas
print(text.upper())       # Convierte todo el texto a mayúsculas
print(text.strip())       # Elimina espacios al inicio y final
print(text.title())       # Convierte la primera letra de cada palabra en mayúscula
print(text.replace("AWESOME", "great"))  # Reemplaza la palabra "AWESOME" por "great"
print(text.split())       # Divide el texto en una lista de palabras separadas por espacio

# ========================================
# Indexación y slicing
# ========================================

word = "programming"

print(word[0])     # 'p'
print(word[-1])    # 'g'
print(word[0:6])   # 'progra'
print(word[:4])    # 'prog'
print(word[4:])    # 'ramming'

# ========================================
# Uso del operador `in` y `not in`
# ========================================

print("gram" in word)      # True
print("hello" not in word) # True

# ========================================
# Iterar sobre un string
# ========================================

for char in "code":
    print(char)

# ========================================
# Uso del método `.find()`
# ========================================

"""
El método `.find(substring)` busca la primera aparición de `substring` en el string.
Devuelve el índice de la primera ocurrencia o -1 si no se encuentra.
"""

text = "Hello, world!"
print(text.find("world"))  # 7
print(text.find("Python"))  # -1

# ========================================
# Uso del método `.join()`
# ========================================

"""
El método `.join(iterable)` une los elementos de un iterable (como una lista) en un solo string,
separándolos por el string que llama al método.
"""

words = ["Python", "es", "genial"]
print(" ".join(words))  # 'Python es genial'

# ========================================
# Uso del método `.format()`
# ========================================

"""
El método `.format()` permite insertar valores en un string utilizando marcadores de posición.
Es útil para crear strings dinámicos y formateados.
"""

name = "Jacob"
age = 25
print("Mi nombre es {} y tengo {} años.".format(name, age))  # 'Mi nombre es Jacob y tengo 25 años.'

# ========================================
# Resumen
# ========================================

"""
## ✅ Resumen:
- Strings son secuencias inmutables de caracteres.
- Métodos comunes: .lower(), .upper(), .strip(), .title(), .replace(), .split().
- Puedes acceder a caracteres con índices (positivos o negativos).
- Puedes usar slicing para obtener partes del string.
- El operador `in` verifica si una subcadena está dentro del string.
- `.find()` devuelve la posición de una subcadena (o -1 si no existe).
- `.join()` une elementos de una lista en un solo string.
- `.format()` permite insertar variables dentro de un string con marcadores {}.
"""

# ========================================
# Ejercicios de Práctica
# ========================================

"""
## 🧠 Ejercicios de práctica con Strings

1️⃣ Crear un string con tu nombre y mostrarlo en mayúsculas.

2️⃣ Eliminar los espacios al inicio y final de un string con `.strip()`.

3️⃣ Reemplazar la palabra "malo" por "bueno" en la frase: "Este código es malo".

4️⃣ Extraer la palabra "data" del string: "bigdata".

5️⃣ Verificar si la palabra "python" está dentro del string "aprendiendo python".
"""

# --------------------------------------------------
# 1️⃣ Crear un string con tu nombre y mostrarlo en mayúsculas
# --------------------------------------------------

name = "Jacob"
print(name.upper())


# --------------------------------------------------
# 2️⃣ Eliminar los espacios al inicio y final de un string con `.strip()`
# --------------------------------------------------

sentence = "    My LAST name is Moronta     "
print(sentence.strip())


# --------------------------------------------------
# 3️⃣ Reemplazar la palabra "malo" por "bueno" en la frase: "Este código es malo"
# --------------------------------------------------
text = "Este codigo es malo"
print(text.replace("malo", "bueno"))


# --------------------------------------------------
# 4️⃣ Extraer la palabra "data" del string: "bigdata"
# --------------------------------------------------

data = "bigdata"
print(data[-4:])


# --------------------------------------------------
# 5️⃣ Verificar si la palabra "python" está dentro del string "aprendiendo python"
# --------------------------------------------------

python = "Aprendiendo python"
print("python" in python)


# --------------------------------------------------
# 6️⃣ Utiliza .find() para encontrar la posición de la palabra "world" en "Hello, world!"
# --------------------------------------------------

char = "Hello, world!"
print(char.find("world"))


# --------------------------------------------------
# 7️⃣ Usa .join() para unir la lista ['Python', 'es', 'asombroso'] con espacios
# --------------------------------------------------

lst = ['Python', 'es', 'asombroso']
print(" ".join(lst))


# --------------------------------------------------
# 8️⃣ Usa .format() para insertar tu nombre y edad en la frase: "Me llamo ___ y tengo ___ años."
# --------------------------------------------------

nombre = "Juan"
edad = 29

print("Me llamo {} y tengo la edad de {}.".format(nombre, edad))
# ========================================

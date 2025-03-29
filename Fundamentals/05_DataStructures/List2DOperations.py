# ========================================
"""
📌 TEMA: Listas 2D en Python

Una lista 2D es una lista que contiene otras listas como elementos. Se comporta como una tabla con filas y columnas.

✅ Características:
- Se accede a los elementos con dos índices: `lista[fila][columna]`.
- Se pueden modificar igual que las listas normales.
- Útiles para representar estructuras como: tablas, calificaciones, menús, etc.
"""
# ========================================


# --------------------------------------------------
# 🎯 Ejemplo 1: Acceder a un valor en una lista 2D
# --------------------------------------------------
"""
Tenemos una lista de estudiantes con sus alturas.
Accederemos a la altura de "Noelle", que está en la fila 0, columna 1.
"""

heights = [["Noelle", 61], ["Ali", 70], ["Sam", 67]]  # Lista 2D con nombres y alturas
noelles_height = heights[0][1]                       # Accedemos a la altura de Noelle
print("Altura de Noelle:", noelles_height)          # Mostramos el resultado


# --------------------------------------------------
# 🎯 Ejemplo 2: Modificar un valor en una lista 2D
# --------------------------------------------------
"""
Tenemos una lista de estudiantes con sus hobbies.
Vamos a cambiar el hobby de Jenny de "Breakdancing" a "Meditation".
"""

class_name_hobbies = [["Jenny", "Breakdancing"], ["Alexus", "Photography"], ["Grace", "Soccer"]]
class_name_hobbies[0][1] = "Meditation"  # Modificamos el valor en la fila 0, columna 1
print("Hobbies después de la modificación:", class_name_hobbies)


# --------------------------------------------------
# 🎯 Ejemplo 3: Recorrer una lista 2D con bucles anidados
# --------------------------------------------------
"""
Tenemos una lista de frutas con sus precios.
Usamos dos bucles for anidados para imprimir cada elemento por separado.
"""

fruits = [["Manzana", 1], ["Banana", 0.5], ["Naranja", 0.75]]

print("Lista de frutas y precios:")
for fruit in fruits:         # Iteramos sobre cada sublista
    for item in fruit:       # Iteramos sobre cada elemento de la sublista
        print(item)          # Imprimimos el elemento


# ========================================
"""
📌 RESUMEN

- Una lista 2D es una lista de listas.
- Se accede a los elementos usando dos índices: `lista[fila][columna]`.
- Se pueden modificar como cualquier otra lista.
- Se pueden recorrer usando bucles for anidados.
"""
# ========================================


# ========================================
"""
## 🧠 Ejercicios de Práctica
Practica tus conocimientos sobre listas 2D resolviendo los siguientes ejercicios.
"""
# ========================================


# --------------------------------------------------
# 1️⃣ Acceso a Calificaciones
# --------------------------------------------------
"""
Crea una lista 2D con estudiantes y sus calificaciones:
students = [["Ana", 90], ["Luis", 85], ["María", 92]]
Luego, accede y muestra por pantalla la calificación de Luis.
"""

# Tu código aquí...


# --------------------------------------------------
# 2️⃣ Modificación de Calificaciones
# --------------------------------------------------
"""
Utiliza la lista del ejercicio anterior y cambia la calificación de Ana a 95.
Luego imprime la lista modificada.
"""

# Tu código aquí...


# --------------------------------------------------
# 3️⃣ Cambio de Precio en el Menú
# --------------------------------------------------
"""
Crea una lista 2D llamada menu:
menu = [["Tacos", 3], ["Burgers", 5], ["Pizza", 8]]
Cambia el precio de "Pizza" a 7.
"""

# Tu código aquí...


# --------------------------------------------------
# 4️⃣ Impresión de Elementos
# --------------------------------------------------
"""
Dada una lista 2D llamada items, usa dos bucles for anidados
para imprimir todos los elementos en pantalla, uno por línea.
"""

# Tu código aquí...


# --------------------------------------------------
# 5️⃣ Agregar un Nuevo Elemento
# --------------------------------------------------
"""
Utiliza la lista menu del ejercicio 3 y agrega un nuevo platillo al final:
["Sushi", 10]
Imprime el resultado final.
"""

# Tu código aquí...

# ========================================

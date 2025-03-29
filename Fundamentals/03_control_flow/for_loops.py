# ========================================
# Uso de For Loops en Python
# ========================================

"""
## 📌 Descripción
Un bucle `for` en Python permite recorrer secuencias como listas, tuplas y diccionarios,
ejecutando un bloque de código por cada elemento.

📌 **Características principales:**
- Se usa principalmente con estructuras iterables.
- Puede combinarse con funciones como `range()`, `enumerate()` y `zip()`.
- Permite el uso de `break`, `continue` y `else` para controlar el flujo de ejecución.
"""

# ========================================
# Ejemplo básico con listas
# ========================================

nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)  # Imprime cada número de la lista

# ========================================
# Uso con tuplas
# ========================================

"""
Las tuplas también son iterables y se pueden recorrer con `for`.
"""
coordenadas = [(1, 2), (3, 4), (5, 6)]
for x, y in coordenadas:
    print(f"Coordenada X: {x}, Coordenada Y: {y}")

# Salida:
# Coordenada X: 1, Coordenada Y: 2
# Coordenada X: 3, Coordenada Y: 4
# Coordenada X: 5, Coordenada Y: 6

# ========================================
# Uso con `range()`
# ========================================

"""
Podemos usar `range()` para iterar sobre una secuencia de números sin definir una lista manualmente.
"""
for i in range(5):
    print(i)  # Salida: 0, 1, 2, 3, 4

# ========================================
# Uso con `enumerate()`
# ========================================

"""
`enumerate()` agrega un índice a cada elemento de la secuencia.
"""
names = ['Alice', 'Bob', 'Charlie']
for index, name in enumerate(names):
    print(f"{index}: {name}")

# ========================================
# Iteración sobre diccionarios
# ========================================

"""
Podemos recorrer claves y valores de un diccionario usando `.items()`.
"""
student_grades = {'John': 90, 'Jane': 88, 'Doe': 92}
for name, grade in student_grades.items():
    print(f"{name} has a grade of {grade}")

# ========================================
# Uso de `zip()` en for
# ========================================

"""
La función `zip()` permite iterar sobre múltiples listas a la vez.
"""

nombres = ["Ana", "Luis", "Carlos"]
edades = [25, 30, 22]

for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años.")

# Salida:
# Ana tiene 25 años.
# Luis tiene 30 años.
# Carlos tiene 22 años.

# ========================================
# Uso de `break`, `continue` y `else`
# ========================================

"""
- `break`: Termina el bucle inmediatamente.
- `continue`: Salta la iteración actual y pasa a la siguiente.
- `else`: Se ejecuta solo si el bucle no se interrumpe con `break`.
"""

# Ejemplo de 'break'
for num in range(10):
    if num == 5:
        break  # Detiene el bucle cuando num es 5
    print(num)
# Salida: 0, 1, 2, 3, 4

# Ejemplo de 'continue'
for num in range(5):
    if num == 2:
        continue  # Omite la impresión del número 2
    print(num)
# Salida: 0, 1, 3, 4

# Ejemplo con else en for-loop
for i in range(5):
    print(i)
else:
    print("Bucle completado sin interrupciones.")

# Si agregamos un break, else no se ejecutará
for num in range(5):
    if num == 3:
        break
    print(num)
else:
    print("Este mensaje no se imprimirá porque el bucle se interrumpió con break.")

# ========================================
# Resumen
# ========================================

"""
## 📌 Resumen
- `for` se usa para recorrer secuencias como listas, cadenas, tuplas y diccionarios.
- `range()` permite generar secuencias de números en bucles.
- `enumerate()` añade índices a elementos iterables.
- `zip()` permite recorrer múltiples listas en paralelo.
- `break` permite salir de un bucle antes de que termine.
- `continue` omite el resto del código en una iteración y pasa a la siguiente.
- `else` en `for` se ejecuta solo si el bucle no se interrumpe con `break`.
"""

# ========================================
# Ejercicios de Práctica
# ========================================

"""
## 🧠 Ejercicios de práctica para For Loops

Practica lo aprendido sobre bucles `for`, `range()`, `enumerate()`, `zip()`, `break`, `continue` y `else`.
Agrega tus propios comentarios dentro de los bloques de código para reforzar lo que aprendiste.
"""

# --------------------------------------------------
# 1️⃣ Imprime los números del 1 al 10
# --------------------------------------------------

for num in range(1, 11):
    print(num)

# --------------------------------------------------
# 2️⃣ Itera una lista de nombres e imprime "Hola, <nombre>"
# --------------------------------------------------

names = ["Angel", "Alicia", "Nicole"]
for name in names:
    print(f"Hola, {name}")

# --------------------------------------------------
# 3️⃣ Usa enumerate() para imprimir el índice y nombre
# --------------------------------------------------

for index, name in enumerate(names):
    print(f"La persona {name}, numero {index}")

# --------------------------------------------------
# 4️⃣ Usa zip() para imprimir nombre y edad
# --------------------------------------------------

edades = [23, 28, 27]
for name, age in zip(names, edades):
    print(f"{name} tiene una edad de {age}")

# --------------------------------------------------
# 5️⃣ Imprime solo los números impares del 1 al 10
# --------------------------------------------------

for number in range(1, 11):
    if number % 2 == 1:
        continue
    print(number)

# --------------------------------------------------
# 6️⃣ Imprime números del 1 al 10 y detén en el 5 con break
# --------------------------------------------------

for numeros in range(1, 11):
    if numeros == 5:
        break
    print(numeros)

# --------------------------------------------------
# 7️⃣ Bucle con else: Imprime 0 a 4, luego un mensaje de éxito
# --------------------------------------------------

for num1 in range(5):
    print(num1)
else:
    print("Exito")

# --------------------------------------------------
# 8️⃣ Recorre una lista de frutas y muestra un mensaje personalizado para cada una
# --------------------------------------------------
lst_fruits = ["Manzana", "Naranja", "Pera", "Limon"]

for lst in lst_fruits:
    if lst == "Manzana":
        print(f"Solo queda una Manzana")
    elif lst == "Naranja":
        print(f"Las naranjas son acidas")
    elif lst == "Pera":
        print(f"No me gustan las peras")
    else:
        print(f"Me gusta el limon con tajin")
# --------------------------------------------------
# 9️⃣ Usa `range()` para imprimir todos los múltiplos de 3 entre 1 y 30
# --------------------------------------------------

def print_multiples_of_3(start, end):
    for number in range(start, end + 1):
        if number % 3 == 0:
            print(f"{number} is a multiple of 3")

result = print_multiples_of_3(1, 30)
print(f"Multiples of 3 are: {result}")
# --------------------------------------------------
# 🔟 Itera sobre una cadena y cuenta cuántas vocales contiene
# --------------------------------------------------
def counting_vowels(txt):
    count = 0
    for char in txt:
        if char.lower() in "aeiou":
            count += 1
    return count

result = counting_vowels("Jacob")
print(f"Cantidad de vocales: {result}")

# --------------------------------------------------
# 1️⃣1️⃣ Usa `zip()` para emparejar una lista de productos con su precio
# --------------------------------------------------
product = ["Honda", "Toyota", "Audi"]
prices = [15600.00, 14800.00, 22350.00]



for car, price in zip(product, prices):
    print(f"{car} prices is {price}")

# --------------------------------------------------
# 1️⃣2️⃣ Usa `enumerate()` para listar los elementos de una lista con su posición en formato 1-based (iniciando desde 1)
# --------------------------------------------------
name_list = ["Jacob", "Nicole", "Juan"]
for index, item in enumerate(name_list, start=1):
    print(f"{index}. {item}")
# --------------------------------------------------
# 1️⃣3️⃣ Recorre una lista de calificaciones y usa `break` si encuentras una calificación menor a 60
# --------------------------------------------------
grades = [80, 79, 61, 57]
for grade in grades:
    if grade < 60:
        break
    print(grade)
# --------------------------------------------------
# 1️⃣4️⃣ Recorre una lista de números del 1 al 20, pero omite los múltiplos de 4 usando `continue`
# --------------------------------------------------

# --------------------------------------------------
# 1️⃣5️⃣ Crea un bucle que sume los números del 1 al 100, y al final imprima "Proceso completado con éxito" si no se usó `break`
# --------------------------------------------------

# ========================================
# Fin del Documento
# ========================================
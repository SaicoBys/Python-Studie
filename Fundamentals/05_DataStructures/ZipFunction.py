# ========================================
# Concepto de zip() en Python
# ========================================

"""
## Descripción
La función `zip()` en Python se usa para combinar múltiples iterables (listas, tuplas, diccionarios, etc.)
en pares ordenados. Devuelve un iterador de tuplas, donde cada tupla contiene elementos de las secuencias
o iterables proporcionados, emparejados según su índice.

Si los iterables tienen diferente longitud, `zip()` detiene el emparejamiento cuando se alcanza
el final del iterable más corto.
"""

# --------------------------------------------------
# 🎯 Ejemplo: zip() con dos listas de igual longitud
# --------------------------------------------------
"""
Usamos zip() para combinar dos listas del mismo tamaño en pares ordenados.
"""
lista1 = [1, 2, 3]  # Primera lista
lista2 = ['a', 'b', 'c']  # Segunda lista
resultado = zip(lista1, lista2)  # Combinamos las dos listas
print(list(resultado))  # [(1, 'a'), (2, 'b'), (3, 'c')]

"""
## Nomenclatura y uso
- `zip(iterable1, iterable2, ...)` → Devuelve un iterador de tuplas con elementos emparejados.
- Se puede convertir el resultado en una lista o tupla usando `list(zip(...))` o `tuple(zip(...))`.
- Si los iterables tienen diferente longitud, `zip()` tomará hasta la longitud del más corto.
"""

# --------------------------------------------------
# 🎯 Ejemplo: zip() con listas de diferente longitud
# --------------------------------------------------
"""
zip() detiene la combinación en la longitud del iterable más corto.
"""
lista1 = [1, 2, 3]  # Primera lista
lista2 = ['a', 'b']  # Segunda lista con menor longitud
resultado = zip(lista1, lista2)  # Combinamos las dos listas
print(list(resultado))  # [(1, 'a'), (2, 'b')]

"""
## Uso con más de dos iterables
Se pueden combinar más de dos iterables al mismo tiempo.
"""

# --------------------------------------------------
# 🎯 Ejemplo: zip() con tres listas
# --------------------------------------------------
"""
Podemos usar zip() con más de dos listas para agrupar múltiples elementos por índice.
"""
numeros = [1, 2, 3]  # Primera lista
letras = ['a', 'b', 'c']  # Segunda lista
simbolos = ['!', '@', '#']  # Tercera lista
resultado = zip(numeros, letras, simbolos)  # Combinamos las tres listas
print(list(resultado))  # [(1, 'a', '!'), (2, 'b', '@'), (3, 'c', '#')]

"""
## Desempaquetado con zip()
La función `zip()` se puede usar junto con el operador `*` para desempaquetar iterables.
"""

# --------------------------------------------------
# 🎯 Ejemplo: Desempaquetado con zip() y *
# --------------------------------------------------
"""
zip() puede desempaquetarse usando el operador * para obtener listas separadas desde una lista de tuplas.
"""
pares = [(1, 'a'), (2, 'b'), (3, 'c')]  # Lista de tuplas
numeros, letras = zip(*pares)  # Desempaquetamos las tuplas en dos listas
print(numeros)  # (1, 2, 3)
print(letras)   # ('a', 'b', 'c')

"""
## Uso en iteración con for
`zip()` es útil en loops cuando se necesita recorrer dos o más listas simultáneamente.
"""

# --------------------------------------------------
# 🎯 Ejemplo: Iteración con zip()
# --------------------------------------------------
"""
Podemos recorrer varias listas a la vez con zip() dentro de un bucle for.
"""
nombres = ['Ana', 'Luis', 'Carlos']  # Lista de nombres
edades = [25, 30, 22]  # Lista de edades

for nombre, edad in zip(nombres, edades):  # Iteramos sobre ambas listas
    print(f"{nombre} tiene {edad} años")  # Imprimimos el mensaje

"""
## Resumen
- `zip()` combina iterables en pares ordenados.
- Se detiene cuando el iterable más corto se agota.
- Puede utilizarse con `*` para desempaquetar.
- Es útil para iteraciones múltiples.
- Devuelve un iterador, por lo que a veces es necesario convertirlo en lista o tupla.
"""

# ========================================
"""
## 🧠 Ejercicios de Práctica
Pon en práctica lo aprendido sobre la función zip().
"""
# ========================================

# --------------------------------------------------
# 1️⃣ Combinar dos listas de colores y códigos hex
# --------------------------------------------------
"""
Crea dos listas: una de colores y otra de códigos hexadecimales.
Combínalas usando zip() y muestra los pares.
"""

# Tu código aquí...


# --------------------------------------------------
# 2️⃣ Iterar sobre tres listas con zip()
# --------------------------------------------------
"""
Crea tres listas: nombres, edades y países.
Recorre las tres listas al mismo tiempo y muestra un mensaje personalizado por cada grupo.
"""

# Tu código aquí...


# --------------------------------------------------
# 3️⃣ Desempaquetar una lista de tuplas con zip()
# --------------------------------------------------
"""
Dada una lista de tuplas de coordenadas [(1, 2), (3, 4), (5, 6)],
desempaquétala en dos listas: una de x y otra de y.
"""

# Tu código aquí...


# ========================================

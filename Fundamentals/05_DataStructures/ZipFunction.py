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

# Ejemplo básico de zip()
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
resultado = zip(lista1, lista2)
print(list(resultado))  # [(1, 'a'), (2, 'b'), (3, 'c')]

"""
## Nomenclatura y uso
- `zip(iterable1, iterable2, ...)` → Devuelve un iterador de tuplas con elementos emparejados.
- Se puede convertir el resultado en una lista o tupla usando `list(zip(...))` o `tuple(zip(...))`.
- Si los iterables tienen diferente longitud, `zip()` tomará hasta la longitud del más corto.
"""

# Ejemplo con diferentes longitudes
lista1 = [1, 2, 3]
lista2 = ['a', 'b']
resultado = zip(lista1, lista2)
print(list(resultado))  # [(1, 'a'), (2, 'b')]

"""
## Uso con más de dos iterables
Se pueden combinar más de dos iterables al mismo tiempo.
"""

# Ejemplo con tres listas
numeros = [1, 2, 3]
letras = ['a', 'b', 'c']
simbolos = ['!', '@', '#']
resultado = zip(numeros, letras, simbolos)
print(list(resultado))  # [(1, 'a', '!'), (2, 'b', '@'), (3, 'c', '#')]

"""
## Desempaquetado con zip()
La función `zip()` se puede usar junto con el operador `*` para desempaquetar iterables.
"""

# Ejemplo de desempaquetado
pares = [(1, 'a'), (2, 'b'), (3, 'c')]
numeros, letras = zip(*pares)
print(numeros)  # (1, 2, 3)
print(letras)   # ('a', 'b', 'c')

"""
## Uso en iteración con for
`zip()` es útil en loops cuando se necesita recorrer dos o más listas simultáneamente.
"""

# Iteración usando zip()
nombres = ['Ana', 'Luis', 'Carlos']
edades = [25, 30, 22]

for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

"""
## Resumen
- `zip()` combina iterables en pares ordenados.
- Se detiene cuando el iterable más corto se agota.
- Puede utilizarse con `*` para desempaquetar.
- Es útil para iteraciones múltiples.
- Devuelve un iterador, por lo que a veces es necesario convertirlo en lista o tupla.
"""

# ========================================

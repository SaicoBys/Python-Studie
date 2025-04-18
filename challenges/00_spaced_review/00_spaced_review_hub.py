# ========================================
# 🔢 BLOQUE 01–10: LISTAS
# ========================================

"""
📚 Conceptos clave:
- Crear listas con []
- Acceder a elementos por índice
- Agregar con .append()
- Eliminar con .pop() o .remove()
- Recorrer listas con for
"""

# ✅ Ejercicio 1: Crear una lista con 3 colores y agregar uno nuevo

# ✅ Ejercicio 2: Imprimir el segundo elemento de la lista

# ✅ Ejercicio 3: Eliminar el último elemento y mostrar la lista resultante

# ✅ Ejercicio 4: Recorrer una lista de frutas e imprimir solo las que tienen más de 5 letras


# ========================================
# 🔤 BLOQUE 11–20: STRINGS
# ========================================

"""
📚 Conceptos clave:
- Métodos: .lower(), .upper(), .strip(), .replace()
- Concatenación de strings
- Slicing [i:j]
- Uso de in para buscar contenido
"""

# ✅ Ejercicio 1: Pedir una palabra al usuario y mostrarla en mayúsculas

word = input("Escribe una palabra:")
def user_input(word):
    upper_word = word.upper()
    return f'Esta es tu palabra en mayúsculas "{upper_word}"'

print(user_input(word))

# ✅ Ejercicio 2: Crear una función que devuelva la cantidad de vocales en un string

def returning_vowels(word):
    vowels = 'AEIOUaeiou'
    vowels_counter = []
    for vowel in vowels:
        if vowel in word:
            vowels_counter.append(vowel)
    return vowels_counter

print(returning_vowels("Jacob"))


# ✅ Ejercicio 3: Mostrar los primeros 3 caracteres de una palabra

def first_three_characters(word):
    three_word = word[:3]
    return f"Las 3 primeras letras de '{word}' son: '{three_word}'"

print(first_three_characters("Jacob"))

# ✅ Ejercicio 4: Concatenar dos strings separados por un espacio

def uniendo_palabras(palabra1, palabra2):
    resultado = palabra1 + " " + palabra2
    return f"Frase resultante: {resultado}"

print(uniendo_palabras("Hola", "Jacob"))


# ========================================
# 🔁 BLOQUE 21–30: LOOPS
# ========================================

"""
📚 Conceptos clave:
- for item in lista
- for i in range(n)
- while condición
- break y continue
"""

# ✅ Ejercicio 1: Imprimir los números del 1 al 10 usando for

def printing_numbers(num1, num2):
    list_numbers = list(range(num1, num2 + 1))
    return list_numbers

print(printing_numbers(1, 10))

# ✅ Ejercicio 2: Contar hacia atrás desde 10 hasta 1 usando while

num1 = 10
while num1 > 0:
    print(num1)
    num1 -= 1


# ✅ Ejercicio 3: Recorre una lista y salta los múltiplos de 3 usando continue

# ✅ Ejercicio 4: Pedir al usuario números hasta que escriba 0 y sumar todos los valores introducidos


# ========================================
# 🧩 BLOQUE 31–40: FUNCIONES
# ========================================

"""
📚 Conceptos clave:
- Definir funciones con def
- Parámetros y argumentos
- Retorno con return
- Funciones dentro de funciones
- Reutilización y claridad del código
"""

# ✅ Ejercicio 1: Escribe una función que reciba un nombre y devuelva "Hola, [nombre]"

def saludar(nombre):
    # Tu código aquí
    pass


# ✅ Ejercicio 2: Escribe una función que reciba dos números y retorne el mayor

def mayor_de_dos(a, b):
    # Tu código aquí
    pass


# ✅ Ejercicio 3: Crea una función que reciba un número y devuelva True si es par, False si es impar

def es_par(numero):
    # Tu código aquí
    pass


# ✅ Ejercicio 4: Escribe una función que reciba una lista de números y devuelva su promedio

def calcular_promedio(lista_numeros):
    # Tu código aquí
    pass


# ✅ Ejercicio 5: Crea una función que reciba una palabra y diga cuántas vocales tiene

def contar_vocales(palabra):
    # Tu código aquí
    pass

# ========================================

# ========================================
# === 001: contar_numeros_pares ===
# ========================================
print("Desafío 001")
"""
📌 CHALLENGE #001: contar_numeros_pares
- Contar la cantidad de números pares en una lista.
- Se itera sobre una lista de números y se verifica si son divisibles entre 2.

🧠 Ejemplo:
Entrada: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Salida esperada: 5
"""
even_count = 0
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in num_list:
    if num % 2 == 0:
        even_count += 1
print(f"Total of even numbers: {even_count}")

# ========================================
# === 002: invertir_string ===
# ========================================
print("Desafío 002")
"""
📌 CHALLENGE #002: invertir_string
- Invertir un string carácter por carácter.
- Se recorre el string desde el último carácter hacia el primero.

🧠 Ejemplo:
Entrada: "python"
Salida esperada: "nohtyp"
"""
word = "python"
for char in range(len(word) - 1, -1, -1):
    print(word[char])

# ========================================
# === 003: sumar_positivos ===
# ========================================
print("Desafío 003")
"""
📌 CHALLENGE #003: sumar_positivos
- Sumar todos los números positivos en una lista.
- Se itera sobre la lista y se omiten los números negativos.

🧠 Ejemplo:
Entrada: [2, -3, -4, 5, -6, 5]
Salida esperada: 7
"""
result = 0
lst = [2, -3, -4, 5, -6, 5]
for num in lst:
    if num < 0:
        continue
    else:
        result += num
print(result)

# ========================================
# === 004: verificar_palindromo ===
# ========================================
print("Desafío 004")
"""
📌 CHALLENGE #004: verificar_palindromo
- Determinar si una palabra es un palíndromo.
- Se invierte la palabra y se compara con la original, ignorando mayúsculas.

🧠 Ejemplo:
Entrada: "Radar"
Salida esperada: True
"""
def is_palindrome(input_word):
    reversed_word = ""
    for index in range(len(input_word) - 1, -1, -1):
        reversed_word += input_word[index]
    if reversed_word.lower() == input_word.lower():
        return True
    return False
print(is_palindrome("Radar"))

# ========================================
# === 005: maximo_tres_numeros ===
# ========================================
print("Desafío 005")
"""
📌 CHALLENGE #005: maximo_tres_numeros
- Encontrar el número máximo entre tres números dados.
- Se comparan los tres números para determinar el mayor.

🧠 Ejemplo:
Entrada: 12, 13, 15
Salida esperada: 15
"""
def max_of_three(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_of_three(12, 13, 15))

# ========================================
# === 006: ordenar_lista ===
# ========================================
print("Desafío 006")
"""
📌 CHALLENGE #006: ordenar_lista
- Ordenar una lista de números en orden ascendente.
- Se utiliza el método sort() para modificar la lista original.

🧠 Ejemplo:
Entrada: [12, 5, 9, 2]
Salida esperada: [2, 5, 9, 12]
"""
def order_list(lst):
    lst.sort()
    return lst
numbers_list = [12, 5, 9, 2]
print(order_list(numbers_list))

# ========================================
# === 007: contar_vocales ===
# ========================================
print("Desafío 007")
"""
📌 CHALLENGE #007: contar_vocales
- Contar la cantidad de vocales en un string dado.
- Se itera sobre el string y se cuentan las letras que son vocales.

🧠 Ejemplo:
Entrada: "Nicole"
Salida esperada: 3
"""
def counting_vowels(word):
    vowels = "aeiou"
    counter = 0
    for index in word:
        if index in vowels:
            counter += 1
    return counter
print(counting_vowels("Nicole"))

# ========================================
# === 008: encontrar_menor_numero ===
# ========================================
print("Desafío 008")
"""
📌 CHALLENGE #008: encontrar_menor_numero
- Encontrar el número más pequeño en una lista.
- Se itera sobre la lista y se compara cada número para encontrar el menor.

🧠 Ejemplo:
Entrada: [12, 5, 9, 2]
Salida esperada: 2
"""
unsorted_list = [12, 5, 9, 2]
def find_smallest(nums):
    minor = nums[0]
    for num in nums:
        if num < minor:
            minor = num
    return minor
print(find_smallest(unsorted_list))

# ========================================
# === 009: invertir_lista ===
# ========================================
print("Desafío 009")
"""
📌 CHALLENGE #009: invertir_lista
- Invertir el orden de los elementos en una lista.
- Se crea una nueva lista y se añaden los elementos en orden inverso.

🧠 Ejemplo:
Entrada: [2, 3, 5, 2, 6, 3, 5]
Salida esperada: [5, 3, 6, 2, 5, 3, 2]
"""
nums = [2, 3, 5, 2, 6, 3, 5]
def reverse_list(lst):
    new_list = []
    for index in range(len(lst) - 1, -1, -1):
        new_list.append(lst[index])
    return new_list
print(reverse_list(nums))

# ========================================
# === 010: buscar_palabra_en_texto ===
# ========================================
print("Desafío 010")
"""
📌 CHALLENGE #010: buscar_palabra_en_texto
- Verificar si una palabra se encuentra dentro de un texto.
- Se utiliza el operador 'in' para determinar la presencia de la palabra.

🧠 Ejemplo:
Entrada: "Jacob", "Hola, Jacob"
Salida esperada: True
"""
def find_word(word, txt):
    if word in txt:
        return True
    return False
print(find_word("Jacob", "Hola, Jacob"))

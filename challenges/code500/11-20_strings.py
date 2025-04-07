# ========================================
# 011: Contar pares y encontrar el máximo en una lista
# ========================================
print("Desafío 011")

"""
📌 DESAFÍO #011: Contar pares y encontrar el máximo en una lista
- Dada una lista de números, cuenta cuántos de ellos son pares y encuentra el número más grande de la lista sin usar funciones predefinidas como max().

🧠 Ejemplo:
Entrada: [3, 6, 2, 5, 10]
Salida esperada:
- Números pares: 3
- Número máximo: 10
"""

def count_evens_and_find_max(lst):
    major = lst[0]
    counter = 0
    for num in lst:
        if num % 2 == 0:
            counter += 1

        if num > major:
            major = num
    return counter, major

entrada = [3, 6, 2, 5, 10]
print(count_evens_and_find_max(entrada))

# ========================================
# 012: Verificar palíndromo con string invertido
# ========================================
print("Desafío 012")

"""
📌 DESAFÍO #012: Verificar palíndromo con string invertido
- Escribe una función que reciba un string, lo invierta y determine si es palíndromo (se lee igual al revés), ignorando mayúsculas/minúsculas.

🧠 Ejemplo:
Entrada: "radar"
Salida esperada: True
"""

palabra = "radar"

def palindrome_inversion(word):
    word_lower = word.lower()
    reversed_word = ""

    for index in range(len(word_lower) - 1, -1, -1):
        reversed_word += word_lower[index]
    
    if word_lower == reversed_word:
        return True
    else:
        return False

print(palindrome_inversion(palabra))

# ========================================
# 013: Sumar los positivos e invertir la lista
# ========================================
print("Desafío 013")

"""
📌 DESAFÍO #013: Sumar los positivos e invertir la lista
- Dada una lista de números, suma únicamente los números positivos y devuelve la lista invertida.

🧠 Ejemplo:
Entrada: [1, -2, 3, 4, -5]
Salida esperada:
- Suma de positivos: 8   (1 + 3 + 4)
- Lista invertida: [-5, 4, 3, -2, 1]
"""

enter = [1, -2, 3, 4, -5]

def sum_positives_reverse_list(lst):
    reversed_list = []
    nums = 0
    for index in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[index])
        if lst[index] > 0:
            nums += lst[index]
    
    message = f"The total is: {nums} and the order is: {reversed_list}"
    return message

print(sum_positives_reverse_list(enter))

# ========================================
# 014: Palíndromo y máximo de tres
# ========================================
print("Desafío 014")

"""
📌 DESAFÍO #014: Palíndromo y máximo de tres
- Crea una función que reciba tres palabras.
- Determina cuál es la palabra más larga (sin usar la función max()).
- Verifica si la palabra más larga es un palíndromo.

🧠 Ejemplo:
Entrada: "ana", "hello", "racecar"
Salida esperada:
- La palabra más larga es "racecar"
- "racecar" es palíndroma: True
"""

def longest_word(word1, word2, word3):
    longest = ""
    length_word1 = len(word1)
    length_word2 = len(word2)
    length_word3 = len(word3)

    if length_word1 > length_word2 and length_word1 > length_word3:
        longest = word1
    elif length_word2 > length_word1 and length_word2 > length_word3:
        longest = word2
    else:
        longest = word3
    is_palindrome = longest == longest[::-1]
    mensaje = f"- La palabra más larga es {longest}"
    mensaje1 = f"- '{longest}' es palíndroma: {is_palindrome}"
    return mensaje + "\n" + mensaje1

print(longest_word("ana", "hello", "racecar"))

# ========================================
# 015: Invertir un string y sumar valores ASCII
# ========================================
print("Desafío 015")

"""
📌 DESAFÍO #015: Invertir un string y sumar valores ASCII
- Dado un string, inviértelo y luego suma el valor ASCII de cada carácter (usa la función ord() para convertir cada carácter a su valor numérico).
- Devuelve ambos resultados: el string invertido y la suma total de los valores ASCII.

🧠 Ejemplo:
Entrada: "Abc"
Salida esperada:
- String invertido: "cbA"
- Suma de valores ASCII: (ord('c') + ord('b') + ord('A'))
"""

def reverse_string_sum_ascii(letter):
    reversed_letter = letter[::-1]
    ascii_sum = 0
    for char in reversed_letter:
        ascii_sum += ord(char)
    return reversed_letter, ascii_sum

print(reverse_string_sum_ascii("abc"))

# ========================================
# 016: extract_domain_from_email
# ========================================
print("Desafío 016")

"""
📌 CHALLENGE #016: extract_domain_from_email
- Escribe una función que reciba una dirección de correo electrónico y retorne su dominio.
- Utiliza el método split() para separar el correo en la parte que aparece después del "@".

🧠 Ejemplo:
Entrada: "user@example.com"
Salida esperada: "example.com"
"""

entrada = "user@example.com"

def extract_domain_from_email(mail):
    return mail.split("@")[-1]

print(extract_domain_from_email(entrada))

# ========================================
# 017: format_greeting_message
# ========================================
print("Desafío 017")

"""
📌 CHALLENGE #017: format_greeting_message
- Escribe una función que reciba dos parámetros: name y city, y retorne un mensaje de saludo formateado.
- Utiliza f-strings o el método format() para insertar las variables en el mensaje.

🧠 Ejemplo:
Entrada: "Ana", "Madrid"
Salida esperada: "Hello, Ana! Welcome to Madrid."
"""

def format_greeting_message(name, city):
    return f"Hello, {name}! Welcome to {city}"

print(format_greeting_message("Jacob", "Santiago."))

# ========================================
# 018: clean_up_string
# ========================================
print("Desafío 018")

"""
📌 CHALLENGE #018: clean_up_string
- Escribe una función que reciba un string con espacios extra al inicio y al final, y retorne el string limpio.
- Utiliza el método strip() para eliminar los espacios en blanco y, si es necesario, el método replace() para corregir errores.

🧠 Ejemplo:
Entrada: "   Hello, wrld!   "
Salida esperada: "Hello, wrld!"  (o "Hello, world!" si se reemplaza "wrld" por "world")
"""

entrada = "   Hello, wrld!   "

def clean_up_string(word):
    return word.strip()

print(clean_up_string(entrada))

# ========================================
# 019: convert_string_to_title_case
# ========================================
print("Desafío 019")

"""
📌 CHALLENGE #019: convert_string_to_title_case
- Escribe una función que reciba un string en minúsculas y lo convierta a title case (la primera letra de cada palabra en mayúscula).
- Utiliza el método title().

🧠 Ejemplo:
Entrada: "the quick brown fox"
Salida esperada: "The Quick Brown Fox"
"""

entrada = "the quick brown fox"

def convert_string_to_title_case(word):
    return word.title()

print(convert_string_to_title_case(entrada))

# ========================================
# 020: search_and_replace_substring
# ========================================
print("Desafío 020")

"""
📌 CHALLENGE #020: search_and_replace_substring
- Escribe una función que reciba un texto y dos cadenas: la subcadena a buscar y la subcadena para reemplazarla.
- Utiliza el método replace() para realizar el cambio.

🧠 Ejemplo:
Entrada: ("The dog is friendly", "dog", "cat")
Salida esperada: "The cat is friendly"
"""

def search_and_replace_substring(txt, word1, word2):
    return txt.replace(word1, word2)

entrada = "The dog is friendly"
print(search_and_replace_substring(entrada, "dog", "cat"))
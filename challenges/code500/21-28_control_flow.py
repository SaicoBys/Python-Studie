# ========================================
# === 021: access_character_by_index ===
# ========================================
print("Desafío 021")
"""
📌 CHALLENGE #021: access_character_by_index
- Escribe una función que reciba un string y un índice, y retorne el carácter en esa posición.
- Recuerda que los índices comienzan en 0.

🧠 Ejemplo:
Entrada: ("Hello", 1)
Salida esperada: "e"
"""

entrada = ("Hello", 1)
def access_character_by_index(char, index):
    return char[index]

print(access_character_by_index(*entrada))

# ======================================== 
# === 022: slice_substring ===
# ========================================
print("Desafío 022")
"""
📌 CHALLENGE #022: slice_substring
- Escribe una función que reciba un string y dos índices (start y end) y retorne la subcadena entre esos índices.
- El slice debe incluir el carácter en el índice start, pero excluir el carácter en el índice end.

🧠 Ejemplo:
Entrada: ("Hello, world!", 7, 12)
Salida esperada: "world"
"""

entrada = ("Hello, world!", 7, 12)
def slice_substring(string, start, end):
    return string[start:end]

print(slice_substring(*entrada))

# ========================================
# === 023: concatenate_strings ===
# ========================================
print("Desafío 023")
"""
📌 CHALLENGE #023: concatenate_strings
- Escribe una función que reciba dos strings y retorne su concatenación.

🧠 Ejemplo:
Entrada: ("Hello", "World")
Salida esperada: "HelloWorld"
"""


# ========================================
# === 024: string_length ===
# ========================================
print("Desafío 024")
"""
📌 CHALLENGE #024: string_length
- Escribe una función que reciba un string y retorne su longitud.
- Puedes utilizar la función len().

🧠 Ejemplo:
Entrada: "Hello"
Salida esperada: 5
"""
# Tu código aquí

# ========================================
# === 025: iterate_string ===
# ========================================
print("Desafío 025")
"""
📌 CHALLENGE #025: iterate_string
- Escribe una función que reciba un string y lo imprima carácter por carácter en líneas separadas utilizando un bucle for.

🧠 Ejemplo:
Entrada: "cat"
Salida esperada:
c
a
t
"""
# Tu código aquí

# ========================================
# === 026: change_case ===
# ========================================
print("Desafío 026")
"""
📌 CHALLENGE #026: change_case
- Escribe una función que reciba un string y retorne una tupla que contenga:
  - El string en minúsculas.
  - El string en mayúsculas.
  - El string en title case.
  
🧠 Ejemplo:
Entrada: "hello world"
Salida esperada: ("hello world", "HELLO WORLD", "Hello World")
"""
# Tu código aquí

# ========================================
# === 027: split_sentence_into_words ===
# ========================================
print("Desafío 027")
"""
📌 CHALLENGE #027: split_sentence_into_words
- Escribe una función que reciba una oración y la divida en una lista de palabras utilizando el método split().

🧠 Ejemplo:
Entrada: "Python is fun"
Salida esperada: ["Python", "is", "fun"]
"""
# Tu código aquí

# ========================================
# === 028: join_words_into_sentence ===
# ========================================
print("Desafío 028")
"""
📌 CHALLENGE #028: join_words_into_sentence
- Escribe una función que reciba una lista de palabras y las una en un solo string, separadas por espacios.
- Utiliza el método join().

🧠 Ejemplo:
Entrada: ["Python", "is", "fun"]
Salida esperada: "Python is fun"
"""
# Tu código aquí
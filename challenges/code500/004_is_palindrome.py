# ========================================
"""
📌 DESAFÍO #004: Verificar si es palíndromo
- Escribe una función que determine si una palabra es un palíndromo (se lee igual al revés).
- Ignora mayúsculas/minúsculas.

🧠 Ejemplo:
Entrada: "Radar"
Salida esperada: True
"""
# ========================================

def is_palindrome(input_word):
    reversed_word = ""
    for index in range(len(input_word) - 1, -1, -1):
        reversed_word += input_word[index]

    if reversed_word.lower() == input_word.lower():
        return True
    return False

print(is_palindrome("Radar"))
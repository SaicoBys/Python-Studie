# ========================================
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
# ========================================

def reverse_string_sum_ascii(letter):
    reversed_letter = letter[::-1]
    ascii_sum = 0
    for char in reversed_letter:
        ascii_sum += ord(char)
    return reversed_letter, ascii_sum

print(reverse_string_sum_ascii("abc"))
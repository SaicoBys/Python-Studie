# ========================================
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
# ========================================

def longest_world(word1, word2, word3):
    longest = ""
    length_word1 = len(word1)
    lenght_word2 = len(word2)
    lenght_word3 = len(word3)

    if length_word1 > lenght_word2 and length_word1 > lenght_word3:
        longest = word1
    elif lenght_word2 > length_word1 and lenght_word2 > lenght_word3:
        longest = word2
    else:
        longest = word3
    is_palindrome = longest == longest[::-1]
    mensaje =  f"- La palabra mas larga es {longest}"
    mensaje1 = f"- '{longest}' es palíndroma: {is_palindrome}"
    return mensaje + "\n" + mensaje1


print(longest_world("ana", "hello", "racecar"))



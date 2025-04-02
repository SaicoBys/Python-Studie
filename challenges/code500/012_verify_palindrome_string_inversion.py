# ========================================
"""
📌 DESAFÍO #012: Verificar palíndromo con string invertido
- Escribe una función que reciba un string, lo invierta y determine si es palíndromo (se lee igual al revés), ignorando mayúsculas/minúsculas.

🧠 Ejemplo:
Entrada: "radar"
Salida esperada: True
"""
# ========================================
palabra = "radar"
def palidrome_inversion(word):
    word_lower = word.lower()
    reversed_word = ""

    for index in range(len(word_lower) - 1, -1, -1):
        reversed_word += word_lower[index]
    
    if word_lower == reversed_word:
        return True
    else:
        return False
    


print(palidrome_inversion(palabra))




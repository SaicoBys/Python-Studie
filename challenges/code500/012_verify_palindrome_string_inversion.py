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
    reversed_word = ""

    for char in range(len(word) - 1, -1, -1):
        reversed_word += word[char]
    
    if word == reversed_word:
        return True , reversed_word
    


print(palidrome_inversion(palabra))




# ========================================
"""
📌 DESAFÍO #010: Buscar palabra en un texto
- Escribe una función que reciba un texto y una palabra, y devuelva `True` si la palabra está presente en el texto.

🧠 Ejemplo:
Entrada: "Hello, how are you?", "how"
Salida esperada: True
"""
# ========================================

def find_word(word, txt):
    if word in txt:
        return True
    return False

print(find_word("Jacob", "Hola, Jacob"))
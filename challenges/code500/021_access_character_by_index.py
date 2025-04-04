# ========================================
"""
📌 CHALLENGE #021: access_character_by_index
- Escribe una función que reciba un string y un índice, y retorne el carácter en esa posición.
- Recuerda que los índices comienzan en 0.

🧠 Ejemplo:
Entrada: ("Hello", 1)
Salida esperada: "e"
"""
# ========================================
entrada = ("Hello", 1)
def access_character_by_index(char, index):
    return char[index]

print(access_character_by_index("Hello", 3))
# ========================================
"""
📌 CHALLENGE #019: convert_string_to_title_case
- Escribe una función que reciba un string en minúsculas y lo convierta a title case (la primera letra de cada palabra en mayúscula).
- Utiliza el método title().

🧠 Ejemplo:
Entrada: "the quick brown fox"
Salida esperada: "The Quick Brown Fox"
"""
# ========================================

entrada = "the quick brown fox"
def convert_string_to_title_case(word):
    return word.title()

print(convert_string_to_title_case(entrada))
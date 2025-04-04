# ========================================
"""
📌 CHALLENGE #020: search_and_replace_substring
- Escribe una función que reciba un texto y dos cadenas: la subcadena a buscar y la subcadena para reemplazarla.
- Utiliza el método replace() para realizar el cambio.

🧠 Ejemplo:
Entrada: ("The dog is friendly", "dog", "cat")
Salida esperada: "The cat is friendly"
"""
# ========================================

def search_and_replace_substring(txt, word1, word2):
    return txt.replace(word1, word2)
entrada = "The dog is friendly"
print(search_and_replace_substring(entrada, "dog", "cat"))
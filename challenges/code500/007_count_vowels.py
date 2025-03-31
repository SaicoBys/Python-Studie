# ========================================
"""
📌 DESAFÍO #007: Contar vocales en un string
- Escribe una función que reciba un string y cuente cuántas vocales (a, e, i, o, u) hay en el string.

🧠 Ejemplo:
Entrada: "hello"
Salida esperada: 2
"""
# ========================================

def counting_vowels(word):
    vowels = "aeiou"
    counter = 0
    for index in word:
        if index in vowels:
            counter += 1
    return counter
        

print(counting_vowels("Nicole"))
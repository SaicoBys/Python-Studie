# ========================================
"""
📌 DESAFÍO #011: Contar pares y encontrar el máximo en una lista
- Dada una lista de números, cuenta cuántos de ellos son pares y encuentra el número más grande de la lista sin usar funciones predefinidas como max().

🧠 Ejemplo:
Entrada: [3, 6, 2, 5, 10]
Salida esperada:
- Números pares: 3
- Número máximo: 10
"""
# ========================================

def count_evens_and_find_max(lst):
    major = lst[0]
    counter = 0
    for num in lst:
        if num % 2 == 0:
            counter += 1

        if num > major:
            major = num
    return counter, major

        


entrada = [3, 6, 2, 5, 10]
print(count_evens_and_find_max(entrada))
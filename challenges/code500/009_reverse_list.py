# ========================================
"""
📌 DESAFÍO #009: Invertir una lista
- Escribe una función que reciba una lista y la devuelva invertida.

🧠 Ejemplo:
Entrada: [1, 2, 3, 4]
Salida esperada: [4, 3, 2, 1]
"""
# ========================================

nums = [2, 3, 5, 2, 6, 3, 5]

def reverse_list(lst):
    new_list = []
    for index in range(len(lst) -1, -1, -1):
        new_list.append(lst[index])
    return new_list
    
print(reverse_list(nums))
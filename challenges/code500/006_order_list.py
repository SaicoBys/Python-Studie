# ========================================
"""
📌 DESAFÍO #006: Ordenar una lista
- Escribe una función que reciba una lista de números y la ordene en orden ascendente.

🧠 Ejemplo:
Entrada: [12, 5, 9, 2]
Salida esperada: [2, 5, 9, 12]
"""
# ========================================

def order_list(lst):
    lst.sort()
    return lst


numbers_list = [12, 5, 9, 2]
print(order_list(numbers_list))
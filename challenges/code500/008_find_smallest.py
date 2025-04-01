# ========================================
"""
📌 DESAFÍO #008: Encontrar el menor número
- Escribe una función que reciba una lista de números y retorne el número más pequeño.

🧠 Ejemplo:
Entrada: [12, 5, 9, 2]
Salida esperada: 2
"""
# ========================================
unsorted_list = [12, 5, 9, 2, 7]

def find_smallest(nums):
    minor = nums[0]
    for num in nums:
        if num < minor:
            minor = num
    return minor

print(find_smallest(unsorted_list))
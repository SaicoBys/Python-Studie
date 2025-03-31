# ========================================
"""
📌 DESAFÍO #005: Máximo de tres números
- Escribe una función que reciba tres números y retorne el mayor de los tres.

🧠 Ejemplo:
Entrada: 4, 9, 2
Salida esperada: 9
"""
# ========================================

def max_of_three(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
print(max_of_three(12, 13, 15))
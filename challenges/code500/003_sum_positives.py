# ========================================
"""
📌 DESAFÍO #003: Sumar los positivos
- Dada una lista de enteros, retorna la suma solo de los números positivos.

🧠 Ejemplo:
Entrada: [-1, 2, -3, 4, -5]
Salida esperada: 6
"""
# ========================================
result = 0
lst = [2, -3, -4, 5, -6, 5]

for num in lst:         # Recorro cada número en la lista para verificar si es positivo
    if num < 0:         # Si el número es negativo, lo omito con continue
        continue
    else:
        result += num   # Si el número es positivo, lo sumo a result
print(result)
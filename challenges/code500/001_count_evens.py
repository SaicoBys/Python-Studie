# ========================================
"""
📌 DESAFÍO #001: Contar números pares
- Dada una lista de números, cuenta cuántos son pares.
- Usa un bucle y condicional para identificar pares.

🧠 Ejemplo:
Entrada: [1, 2, 3, 4, 5, 6]
Salida esperada: 3
"""
# ========================================

even_count = 0
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in num_list:            # Recorro la lista de números uno por uno.
    if num % 2 == 0:            # Verifico si el número es divisible entre 2 (par).
        even_count += 1         # Incremento el contador si el número es par.

print(f"Total of even numbers: {even_count}")
    
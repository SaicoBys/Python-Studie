# ========================================
"""
📌 DESAFÍO #002: Invertir un string
- Escribe una función que reciba un string y retorne su versión invertida.
- Usa slicing o un bucle.

🧠 Ejemplo:
Entrada: "python"
Salida esperada: "nohtyp"
"""
# ========================================

word = "python"  # Asignamos el string "python" a la variable `word`

# Recorremos el string desde el último carácter hacia el primero
for char in range(len(word) - 1, -1, -1):  
    # `range(len(word) - 1, -1, -1)` es el rango de índices para recorrer el string desde el final.
    # El primer -1 indica el inicio en el último índice del string (len(word) - 1)
    # El segundo -1 indica el final del rango, que es antes de llegar a `-1` (esto permite incluir el primer carácter, que tiene índice 0)
    # El tercer -1 es el paso, indicando que estamos recorriendo los índices de atrás hacia adelante (en orden inverso).

    print(word[char])  # Imprime cada carácter en orden inverso. La variable `char` contiene el índice de cada carácter a imprimir.
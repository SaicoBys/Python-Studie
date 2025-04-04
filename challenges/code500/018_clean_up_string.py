# ========================================
"""
📌 CHALLENGE #018: clean_up_string
- Escribe una función que reciba un string con espacios extra al inicio y al final, y retorne el string limpio.
- Utiliza el método strip() para eliminar los espacios en blanco y, si es necesario, el método replace() para corregir errores.

🧠 Ejemplo:
Entrada: "   Hello, wrld!   "
Salida esperada: "Hello, wrld!"  (o "Hello, world!" si se reemplaza "wrld" por "world")
"""
# ========================================
entrada =  "   Hello, wrld!   "
def clean_up_string(word):
    return word.strip()

print(clean_up_string(entrada))


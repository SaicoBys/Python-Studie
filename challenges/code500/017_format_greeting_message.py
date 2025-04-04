# ========================================
"""
📌 CHALLENGE #017: format_greeting_message
- Escribe una función que reciba dos parámetros: name y city, y retorne un mensaje de saludo formateado.
- Utiliza f-strings o el método format() para insertar las variables en el mensaje.

🧠 Ejemplo:
Entrada: "Ana", "Madrid"
Salida esperada: "Hello, Ana! Welcome to Madrid."
"""
# ========================================

def format_greeting_message(name, city):
    return f"Hello, {name}! Welcome to {city}"

print(format_greeting_message("Jacob", "Santiago."))
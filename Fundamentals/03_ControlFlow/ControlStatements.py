# ========================================
# Control de Flujo en Bucles: Break y Continue
# ========================================

"""
## 📌 Descripción
Las declaraciones `break` y `continue` se usan para modificar el flujo de control dentro de los bucles.

📌 **Diferencias principales:**
- `break` **detiene** el bucle inmediatamente.
- `continue` **omite** el resto del código en la iteración actual y pasa a la siguiente.

📌 **Casos de uso comunes:**
- `break`: Se usa cuando encontramos un resultado específico y queremos salir del bucle.
- `continue`: Se usa cuando queremos omitir ciertas iteraciones sin detener el bucle por completo.
"""

# ========================================
# Uso de 'break' en una búsqueda
# ========================================

"""
`break` se usa cuando queremos detener un bucle una vez que encontramos un resultado específico.
"""

nombres = ["Ana", "Luis", "Carlos", "Elena"]
nombre_buscado = "Carlos"

for nombre in nombres:
    if nombre == nombre_buscado:
        print(f"Encontrado: {nombre}")
        break  # Se detiene la búsqueda una vez encontrado
    print(f"Buscando... {nombre}")

# Salida:
# Buscando... Ana
# Buscando... Luis
# Encontrado: Carlos

# ========================================
# Uso de 'continue' para omitir elementos
# ========================================

"""
`continue` se usa cuando queremos omitir ciertas iteraciones sin detener el bucle.
"""

usuarios = [
    {"nombre": "Ana", "activo": True},
    {"nombre": "Luis", "activo": False},
    {"nombre": "Carlos", "activo": True},
    {"nombre": "Elena", "activo": False},
]

for usuario in usuarios:
    if not usuario["activo"]:
        continue  # Salta los usuarios desactivados
    print(f"Enviando notificación a {usuario['nombre']}")

# Salida:
# Enviando notificación a Ana
# Enviando notificación a Carlos

# ========================================
# Uso de 'break' en un bucle for con números
# ========================================

"""
Podemos usar `break` para detener la ejecución de un bucle cuando se cumpla una condición.
"""

for num in range(10):
    if num == 5:
        print("Número 5 encontrado, saliendo del bucle.")
        break  # Se detiene la ejecución cuando num es 5
    print(num)

# Salida: 0, 1, 2, 3, 4, "Número 5 encontrado, saliendo del bucle."

# ========================================
# Uso de 'continue' en un bucle for con números
# ========================================

"""
Podemos usar `continue` para saltar iteraciones en un bucle.
"""

for num in range(10):
    if num % 2 == 0:
        continue  # Salta los números pares
    print(num)

# Salida: 1, 3, 5, 7, 9

# ========================================
# Resumen
# ========================================

"""
## 📌 Resumen
- `break` permite salir de un bucle inmediatamente cuando se cumple una condición.
- `continue` omite el resto del código en una iteración y pasa a la siguiente.
- Se pueden usar en bucles `for` y `while` para controlar la ejecución.
- `break` es útil para detener búsquedas o procesos cuando se encuentra un resultado.
- `continue` es útil para omitir elementos no deseados sin detener el bucle.
"""

# ========================================
# Ejercicios de Práctica
# ========================================

"""
## 🧠 Ejercicios de práctica para Break y Continue

1️⃣ Buscar el primer múltiplo de 7 (break). Recorre una lista de números del 1 al 20. Detén el bucle al encontrar el primer múltiplo de 7.

2️⃣ Imprimir del 1 al 10 omitiendo múltiplos de 3. Imprime los números del 1 al 10, pero omite los múltiplos de 3.

3️⃣ Buscar un nombre en una lista y detenerse al encontrarlo. Recorre una lista de nombres y detén el bucle cuando encuentres "Elena".

4️⃣ Filtrar usuarios activos. Crea una lista de usuarios con un campo "activo". Imprime solo los nombres de los usuarios activos (usa continue). (Este ejercicio será desarrollado cuando veas diccionarios)

5️⃣ Detener bucle al llegar a 10. Imprime los números del 1 al 15. Si el número es 10, muestra "Interrumpido en 10" y termina el bucle.

✅ Prueba a resolver cada uno con lo aprendido sobre `break` y `continue`.
"""

# --------------------------------------------------
# 1️⃣ Buscar el primer múltiplo de 7 (break)
# --------------------------------------------------

for num in range(1, 21):
    if num % 7 == 0:
        print(f"El número {num} es múltiplo de 7")
        break
    else:
        print(f"Buscando... {num}")

# --------------------------------------------------
# 2️⃣ Imprimir del 1 al 10 omitiendo múltiplos de 3
# --------------------------------------------------

for multi in range(1, 11):
    if multi % 3 == 0:
        continue
    print(f"{multi} no es múltiplo de 3")

# --------------------------------------------------
# 3️⃣ Buscar un nombre en una lista y detenerse al encontrarlo
# --------------------------------------------------

nombres = ["Jacob", "Nicole", "Alejandrina", "Elena", "Fabiola", "Tatis"]
buscar = "Elena"

for nombre in nombres:
    if nombre == buscar:
        print(f"Nombre encontrado: {nombre}")
        break
    else:
        print(nombre)

# --------------------------------------------------
# 4️⃣ Filtrar usuarios activos
# --------------------------------------------------

# 🔒 Este ejercicio requiere diccionarios. Lo resolveremos más adelante:
# usuarios = [{"nombre": "Ana", "activo": True}, ...]

# --------------------------------------------------
# 5️⃣ Detener bucle al llegar a 10
# --------------------------------------------------

for numero in range(1, 16):
    if numero == 10:
        print("Interrumpido en 10")
        break
    print(numero)

# ========================================
# Fin del Documento
# ========================================